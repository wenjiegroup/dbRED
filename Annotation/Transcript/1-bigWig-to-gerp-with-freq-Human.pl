use strict;
my $uniqueBed="$ARGV[0]_unique.bed";
my $hg19_gerp="/public2/home/zhaoch/annovar/reference/hg19.100way.phastCons.bw";
my $output="./the_gerp_of_editings.txt ";
my $outbed="./the_gerp_of_editings.bed";
my $result="$ARGV[0]_gerp.txt";
my $bigwig="/public2/home/zhaoch/annovar/reference/bigWigAverageOverBed";

system("$bigwig $hg19_gerp $uniqueBed $output -bedOut=$outbed");
my @a;
open(o1,">$result")||die"error $result\n";
#print o1 "chro\tpos\tgerp\n";
open(f,$outbed)||die"error $outbed\n";
while(<f>)
{
	@a=split/\s+/,$_;
	print o1 "$a[0]\t$a[2]\t$a[4]\n";
}
close f;
close o1;
#system("rm $output $outbed");
