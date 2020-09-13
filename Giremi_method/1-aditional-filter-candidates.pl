use strict;

my $GATK="/public2/home/zhaoch/local/GenomeAnalysisTK.jar";
my $hg="/public2/home/zhaoch/Reference_data/ucsc.hg19.fasta";



my $DPcut = 5;
my $ALTcut = 3;
my $AFup = 0.95;
my $AFdown = 0.1;

my $indir = "/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $input = "/$ARGV[0]";#"./ERR188203.gatk.vcf"
my $outdir = "/public2/home/zhaoch/Giremi_method/$ARGV[0]";#"./Mapping_dir/$input/";
if (!-e $outdir){mkdir $outdir;}


open (o2,">$outdir$input.filter.report") || die "error $outdir$input.filter.vcf\n";
print o2 "Sample\tTotal\tpass\tDPfil\tALTfil\tAFfil\tStrandfil\n";

open (f1,"$indir$input.gatk.vcf") || die "Erorr $input.gatk.vcf\n";
my $number1 = 1;
while(<f1>)
{
	next if ($_=~/\#/);
	#last if ($number > 50);
	chomp;
	my @list = split /\t/,$_;
	my %attr=();
	$attr{"CHROM"}=$list[0];
	$attr{"POS"}=$list[1];
	my $end = $list[1]+1;
	$attr{"REF"}=$list[3];
	$attr{"ALT"}=$list[4];
	#dele indel
	next if (length($list[3]) > 1 || length($list[4]) > 1 || $list[0] eq "chrM" || length($list[0]) > 5); 
	$number1++;
}
close f1;
print o2 "$input\t$number1\t";
print "$input\t$number1\t";

#system ("java -Xmx16g -jar $GATK -R $hg -T VariantFiltration -V ./ERR188203.gatk.raw.vcf -window 35 -cluster 3 -filterName FS -filter \"FS > 30.0\" -filterName QD -filter \"QD < 2.0\" -o ./ERR188203.VariantFiltration.vcf");#*.gatk.vcf文件中已经过滤了lowQual/FD等位点

open (o1,">$outdir$input.filter.vcf") || die "error $outdir$input.filter.vcf\n";

open (f1,"$indir$input.gatk.vcf") || die "Error $input.gatk.vcf";
my ($DPfil,$ALTfil,$AFfil,$Strandfil,$pass);
my $number2=1;
while (<f1>)
{
	next if ($_=~/\#/);
	#last if ($number > 50);
	chomp;
	my @list = split /\t/,$_;
	my %attr=();
	$attr{"CHROM"}=$list[0];
	$attr{"POS"}=$list[1];
	my $end = $list[1]+1;
	$attr{"REF"}=$list[3];
	$attr{"ALT"}=$list[4];
	#delete indel
	next if (length($list[3]) > 1 || length($list[4]) > 1 || $list[0] eq "chrM" || length($list[0]) > 5); 
	$number2++;
	#remove sites with DP<5, ALT<3, ExtremeAF, strand biased.
	my @attributes = split /;/, $list[7];
	foreach my $attr ( @attributes) 
	{
		if ($attr =~ /^(\S+)\=(\S+)$/) 
		{
			my $c_type  = $1;
			my $c_value = $2;
			$attr{$c_type} = $c_value;
			my @c_value=split /\,/,$c_value;
			for (my $j=0;$j<@c_value;$j++)
			{
				$attr{"$c_type$j"}=$c_value[$j];
			}
		}
	}
	my ($ref,$alt);
	for (my $listID=9;$listID<scalar(@list);$listID++)
	{
		my @AD = split /:|,/,$list[$listID];
		$ref=$ref+$AD[1];
		$alt=$alt+$AD[2];
	}
	my $strand;
	my $AF;
	if ($ref+$alt == 0){
		next;
	}
	$AF = $alt/($ref+$alt);
	

	if ($alt < $ALTcut){$ALTfil++;}
	if ($ref+$alt < $DPcut){$DPfil++;}
	if ($AF > $AFup || $AF < $AFdown){$AFfil++;}
	
	if ($ref+$alt < $DPcut || $alt < $ALTcut || $AF > $AFup || $AF < $AFdown){next;}# || $strand < $strandCut
	print o1 "$list[0]\t$list[1]\t$end\t$list[3]\t$list[4]\t$AF\n";$pass++;
	
}
$Strandfil = $number1-$number2;
print o2 "$pass\t$DPfil\t$ALTfil\t$AFfil\t$Strandfil\n";
print "$pass\t$DPfil\t$ALTfil\t$AFfil\t$Strandfil\n";
close f1;
close o1;
close o2;