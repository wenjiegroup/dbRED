use strict;

my $outdir = "/public2/home/zhaoch/Giremi_method/$ARGV[0]";
my $input = $ARGV[0];#"ERR188203";
my $samtools="/public2/home/zhaoch/local/samtools-1.3.1/samtools";
my $Reference="/public2/home/zhaoch/Reference_data/ucsc.hg19";
my $dbSNP="/public2/home/zhaoch/Reference_data/dbsnp_137.hg19.vcf";
my $GIREMI = "./giremi";
my $GeneAnno="/public2/home/zhaoch/Reference_data/gencode.v25lift37.annotation.gtf.geneInterval";
my $AnnoDir = "/public2/home/zhaoch/Reference_data/";
my $bedtools = "/public2/home/zhaoch/local/bedtools2/bin/bedtools";
my $bedops = "/home/lihao/bedops_bin";



print "$input\n";

print "Gene Annotation ...\n";
system ("$bedtools intersect -a $outdir/$input.filter.vcf  -b $GeneAnno -wb > $outdir/$input.VariantsInGene.temp");
my %geneInfo;
my $chr;
my $InGeneNumber;



open (f1,"$outdir/$input.VariantsInGene.temp") || die "Error";
while (<f1>)
{
	$_=~s/\s+$//;
	my $line = $_;
	my @a = split /\t/,$_;
	my $pos = $a[1];
	$geneInfo{$a[0]."\t".$a[1]} = $a[10]."\t".$a[9];
	close f2;
}
close f1;


#whether is dbSNP
print "Read dbSNP ...\n";
open (f1,"$dbSNP") || die "Error";
my %dbSNP;
while (<f1>)
{
	my @a = split /\t/,$_;
	my $b = join "\t",$a[0],$a[1];
	$dbSNP{$b} = 1;
}
close f1;
open (f1,"$outdir/$input.filter.vcf") || die "Error";
open (o1,">$outdir/$input.INPUT") || die "Error";
my $dbSNPnumber;
while (<f1>)
{
	$_=~s/\s+$//;
	my @a = split /\t/,$_;
	my $gene = $geneInfo{$a[0]."\t".$a[1]};
	my $b = join "\t",$a[0],$a[1];
	my $start = $a[1]-1;
	print o1 "$a[0]\t$start\t$a[1]\t";
	my $Snp;
	if ($dbSNP{$b} eq ""){$Snp = 0;}
	else {$Snp = 1;$dbSNPnumber++;}
	if ($gene eq ""){print o1 "Inte\t$Snp\t#\n";}
	else {
		my @b  =split /\t/,$gene;
		print o1 "$b[0]\t$Snp\t$b[1]\n";
	}
}
close f1;
close o1;
