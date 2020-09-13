use strict;

my $picard="/public2/home/zhaoch/local/picard-tools-1.141/picard.jar";
my $indir="/public2/home/zhaoch/STAR_mapping_dir/";
my $outdir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]/";
my $samtools="/public2/home/zhaoch/local/samtools-1.3.1/samtools";
if(!(-e $outdir)){mkdir $outdir or die};
## For pooled-method in JinBilly Li. We merge alignments from all repeats.
#repeat Step 2, then merge sort.bam file 
#system("java -jar $picard/MergeSamFiles.jar INPUT=$input1.sort.bam INPUT=$input2.sort.bam OUTPUT=$input.sort.bam SO=coordinate VALIDATION_STRINGENCY=SILENT");
my $ord = "java -jar $picard MergeSamFiles ";
for(my $i=1;$i<@ARGV;$i++)
{
	$ord = "$ord INPUT=$indir$ARGV[$i]/$ARGV[$i].recal.bam ";
}
$ord = "$ord OUTPUT=$outdir$ARGV[0].merge.bam SO=coordinate VALIDATION_STRINGENCY=SILENT";
system($ord);
system("$samtools index $outdir$ARGV[0].merge.bam");