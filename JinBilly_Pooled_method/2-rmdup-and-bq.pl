##remove duplicates and  filter mapping quality
my $input="/$ARGV[0]";#input file name 
my $cell="$ARGV[1]";
my $outdir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $samtools="/public2/home/zhaoch/local/samtools-1.3.1/samtools";
my $picard="/public2/home/zhaoch/local/picard-tools-1.141/picard.jar";

system("java -Xmx31g -jar $picard AddOrReplaceReadGroups I=$outdir$input.recal.bam O=$outdir$input.addrecal.bam SO=coordinate RGID=$cell RGLB=$cell RGPL=illumina RGPU=illumina RGSM=$cell VALIDATION_STRINGENCY=SILENT");

