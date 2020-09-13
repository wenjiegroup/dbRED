##remove duplicates and  filter mapping quality
my $input="/$ARGV[0]";#input file name 
my $cell="$ARGV[1]";
my $outdir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $samtools="/public2/home/zhaoch/local/samtools-1.3.1/samtools";
my $picard="/public2/home/zhaoch/local/picard-tools-1.141/picard.jar";

#-----------------BOX2 | Quality Control of Mapping Reads.
#Step 1: Remove duplicates reads.
system("java -Xmx31g -jar $picard AddOrReplaceReadGroups I=$outdir$input.sort.bam O=$outdir$input.head.bam SO=coordinate RGID=ABRF RGLB=ABRF RGPL=illumina RGPU=illumina RGSM=ABRF VALIDATION_STRINGENCY=SILENT");

system("java -Xmx31g -jar $picard MarkDuplicates MAX_FILE_HANDLES_FOR_READ_ENDS_MAP=2000 INPUT=$outdir$input.head.bam OUTPUT=$outdir$input.dedup.sam METRICS_FILE=$outdir$input.dedup.matrix CREATE_INDEX=true VALIDATION_STRINGENCY=LENIENT REMOVE_DUPLICATES=true");

#Step 2: Convert the position of reads that map across splicing junctions. Not required for Tophat maping. 
##-------------if reads are mapped to splicing junction reference, we need to change the coordinates 
#system("javac convertCoordinates.java");
#system("java -Xmx31g convertCoordinates < $outdir$input.dedup.sam > $outdir$input.java.sam");
##-------------------------------------------
#Step 3: Filter out unmapped reads and reads with MQ < 20.
system("$samtools view -Sq 20 -h $outdir$input.dedup.sam -o $outdir$input.bq.sam");
system("$samtools view -bS $outdir$input.bq.sam -o $outdir$input.bq.bam");
system("$samtools index $outdir$input.bq.bam");

#system("rm $outdir$input.trimmed.fastq   $outdir$input.trimmed_single_file.fastq ");
