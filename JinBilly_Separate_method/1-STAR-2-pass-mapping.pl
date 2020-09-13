use strict;

my $sickle="/public2/home/zhaoch/local/sickle-master/sickle";
my $STAR="/public2/home/zhaoch/local/STAR-2.5.2b/bin/Linux_x86_64/STAR";
my $picard="/public2/home/zhaoch/local/picard-tools-1.141/picard.jar";
my $reference="/public2/home/zhaoch/Reference_data/ucsc.hg19.fasta";
my $gtf="/public2/home/zhaoch/Reference_data/gencode.v25lift37.annotation.gtf";
my $indir="$ARGV[0]";
my $outdir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[1]/";
my $input="$ARGV[1]";
my $input2="$ARGV[6]";
my $length=$ARGV[3]-1;#readLength-1
my $threads=$ARGV[2];
my $genomeDir="/public2/home/zhaoch/Reference_data/index$length";
my $file_type=$ARGV[4];
my $ctype = $ARGV[5];

if(!(-e $genomeDir)){mkdir $genomeDir or die};
#Step 1. generate genome index

system("$STAR --runMode genomeGenerate --genomeDir $genomeDir --genomeFastaFiles $reference --runThreadN $threads --sjdbGTFfile $gtf --sjdbOverhang $length");

#Step 2. 2-pass mapping
if(!(-e $outdir)){mkdir $outdir or die};

#pair_end fastq
if($file_type eq "pair_end"){
	if($ctype eq "tgz"){
	print "start run tgz";
	system("$sickle pe -t sanger -q 20 -n -f $indir$input.fastq.tgz -r $indir$input2.fastq.tgz -o $outdir$input.trimmed.fastq -p $outdir$input2.trimmed.fastq -s $outdir$input.trimmed_single_file.fastq ");
	}
	elsif($ctype eq "gz"){
        system("$sickle pe -t sanger -q 20 -n -f $indir$input.fastq.gz -r $indir$input2.fastq.gz -o $outdir$input.trimmed.fastq -p $outdir$input2.trimmed.fastq -s $outdir$input.trimmed_single_file.fastq ");
        }
        else{
        system("$sickle pe -t sanger -q 20 -n -f $indir$input.fastq -r $indir$input2.fastq -o $outdir$input.trimmed.fastq -p $outdir$input2.trimmed.fastq -s $outdir$input.trimmed_single_file.fastq ");
        }
#automatic  2-pass mapping
	system("$STAR --outFileNamePrefix $outdir$input --genomeDir $genomeDir --readFilesIn $outdir$input.trimmed.fastq $outdir$input2.trimmed.fastq --twopassMode Basic --runThreadN $threads");
}

#single_end
if($file_type eq "single_end"){
	if($ctype eq "tgz"){
	system("$sickle se -t sanger -q 20 -n -f $indir$input.fastq.tgz -o $outdir$input.trimmed.fastq");
	}
	elsif($ctype eq "gz"){
        system("$sickle se -t sanger -q 20 -n -f $indir$input.fastq.gz -o $outdir$input.trimmed.fastq");
        }
        else{
        system("$sickle se -t sanger -q 20 -n -f $indir$input.fastq -o $outdir$input.trimmed.fastq");
        }
        system("$STAR --outFileNamePrefix $outdir$input --genomeDir $genomeDir --readFilesIn $outdir$input.trimmed.fastq --twopassMode Basic --runThreadN $threads");
}

##----separate method
system("java -Xmx24g -jar $picard SortSam INPUT=$outdir$input\Aligned.out.sam OUTPUT=$outdir$input.sort.bam SORT_ORDER=coordinate VALIDATION_STRINGENCY=SILENT");


## For pooled-method in JinBilly Li. We merge alignments from all repeats.
#repeat Step 2, then merge sort.bam file 
system("java -jar $picard/MergeSamFiles.jar INPUT=$input1.sort.bam INPUT=$input2.sort.bam OUTPUT=$input.sort.bam SO=coordinate VALIDATION_STRINGENCY=SILENT");

