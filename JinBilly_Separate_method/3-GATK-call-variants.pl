use strict;
#GATK call variants


my $samtools="/public2/home/zhaoch/local/samtools-1.3.1/samtools";
my $GATK="/public2/home/zhaoch/local/GenomeAnalysisTK.jar ";
my $Reference="/public2/home/zhaoch/Reference_data/ucsc.hg19";
my $dbsnp="/public2/home/zhaoch/Reference_data/dbsnp_137.hg19.vcf";
my $indir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $outdir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $input="/$ARGV[0]";#input file name 
my $script="/public2/home/zhaoch/RNA_editing_script_for_Zhaochenghui/RNA_editing_method/Transcript";

if(!(-e $outdir)){mkdir $outdir or die;}


system("java -Xmx31g -jar $GATK -T SplitNCigarReads -R $Reference.fasta -I $indir$input.bq.bam -o $outdir$input.split.bam -rf ReassignOneMappingQuality -RMQF 255 -RMQT 60 -U ALLOW_N_CIGAR_READS --fix_misencoded_quality_scores");

system("java -Xmx31g -jar $GATK -R $Reference.fasta -T RealignerTargetCreator  -o $outdir$input.realn.intervals -I $outdir$input.split.bam");

system("java -Xmx31g -jar $GATK -R $Reference.fasta -T IndelRealigner -targetIntervals $outdir$input.realn.intervals -I $outdir$input.split.bam -o $outdir$input.realn.bam "); 
#=cut;
system("java -Xmx31g -jar $GATK -R $Reference.fasta -T BaseRecalibrator -I $outdir$input.realn.bam -knownSites $dbsnp -o $outdir$input.recal_data.grp "); 
system("java -Xmx31g -jar $GATK -R $Reference.fasta -T PrintReads -I $outdir$input.realn.bam  -o $outdir$input.recal.bam -BQSR $outdir$input.recal_data.grp");

#-------------------BOX4 | Process to identify mismatches in RNA-seq reads.
system("java -jar -Xmx31g $GATK -R $Reference.fasta -T HaplotypeCaller -I $outdir$input.recal.bam -o $outdir$input.haplo.vcf --dbsnp $dbsnp  -stand_call_conf 20 -stand_emit_conf 0 -dontUseSoftClippedBases");

system("java -jar -Xmx31g $GATK -T VariantFiltration -R $Reference.fasta -V $outdir$input.haplo.vcf -window 35 -cluster 3 -filterName FS -filter \"FS > 30.0\" -filterName QD -filter \"QD < 2.0\" --invalidatePreviousFilters -o $outdir$input.gatk.raw.vcf ");

system("rm $outdir$input.*.sam $outdir$input\Aligned.out.sam");
