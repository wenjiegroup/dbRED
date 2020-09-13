use strict;

my $GIREMI = "/public2/home/zhaoch/RNA_editing_script_for_Zhaochenghui/Giremi_method/giremi";
my $Reference = "/public2/home/zhaoch/Reference_data/Mus_musculus.GRCm38.85.chr1-Y.fasta";
my $indir = "/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $outdir = "/public2/home/zhaoch/Giremi_method/$ARGV[0]";
my $input=$ARGV[0];
my $bamInput="$indir/$ARGV[1]";#"./$input.recal.bam";
my $dataType=$ARGV[2];#1:paired-end; 0:single-end
my @a;

# run Giremi.pl
system ("$GIREMI -f $Reference -l $outdir/$input.INPUT -p $dataType -s 0 -o $outdir/$input.GIREMI $bamInput");

#-s, --strand     INT          0:non-strand specific RNA-Seq; 1: strand-specific RNA-Seq and read 1 (first read for the paired-end reads) is sense to RNA; 2: strand-specific RNA-Seq and read 1 is anti-sense to RNA [default: 0]


open(o,">$outdir/$input.GIREMI.RNAediting.txt");
open(f,"$outdir/$input.GIREMI.res")||die"error open $input.GIREMI.res\n";
while(<f>)
{
	@a = split/\s+/,$_;
	if($a[-1] != 0)
	{
		#print o $_;
		my @b=split//,$a[17];
		print o "$a[1]\t$a[2]\t$b[0]\t$b[1]\n";
	}
}
close f;
close o;
