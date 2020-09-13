use strict;
my $script="/public2/home/zhaoch/RNA_editing_script_for_Zhaochenghui/RNA_editing_method/Transcript";
my $bedtools="/public2/home/zhaoch/local/bedtools2/bin/bedtools";
my $samtools="/public2/home/zhaoch/local/samtools-1.3.1/samtools";
my $input="/$ARGV[0]";
my $indir="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[0]";
my $outdir="/public2/home/zhaoch/JinBilly_method_single/$ARGV[0]";
my $Reference="/public2/home/zhaoch/Reference_data/ucsc.hg19";
my $dbsnp="/public2/home/zhaoch/Reference_data/dbsnp_137.hg19.vcf";


my $cdna="RNA_editing_method/Transcript/hg19-data/snp_cdna.txt";
my $Alu="RNA_editing_method/Transcript/hg19-data/Alu.sort.txt";
my $simple="RNA_editing_method/Transcript/hg19-data/simple_repeats.sort.txt";
my $anno="RNA_editing_method/Transcript/hg19-data/Ensembl_gene_annotation.txt";
my $non_Alu="RNA_editing_method/Transcript/hg19-data/non-Alu.fin.txt";
my $threads=$ARGV[1];


##JinBilly Li filtering method
system("perl ./1-STAR-2-pass-mapping.pl $ARGV[0] $threads");
system("perl ./2-rmdup-and-bq.pl $ARGV[0]");
system("perl ./3-GATK-call-variants.pl $ARGV[0]");
if(!(-e $outdir)){mkdir $outdir or die;}
#system("rm $outdir$input.realn.bam");

system("perl $script/Convert_VCF.pl $indir$input.gatk.vcf $outdir$input.con.vcf");

system("perl $script/ref_filter.pl $cdna $outdir$input.con.vcf $indir$input.gatk.vcf $outdir$input.ref.vcf ");

system("perl $script/threads_rmMismatch.pl $outdir$input.ref.vcf  $indir$input.recal.bam $outdir$input.rem.vcf $threads");

system("perl $script/Alu_filter.pl $Alu $outdir$input.rem.vcf $outdir$input.Alu.vcf $outdir$input.nonAlu.vcf");

system("perl $script/FreqSimple.pl $simple $outdir$input.nonAlu.vcf  $outdir$input.sim.vcf");

system("perl $script/threads_rmSJandHomo.pl $Reference.fasta $outdir$input $anno $threads");

system("perl $script/threads_BlatCandidates.pl $Reference.fasta $outdir$input.rmSJandHomo.txt $indir$input.recal.bam $outdir$input.blat.vcf $threads");

system("perl $script/nonAlu_filter_new.pl $non_Alu $outdir$input.blat.vcf $outdir$input.RepAlu.vcf $outdir$input.nonRep.vcf");

system("cat $outdir$input.Alu.vcf $outdir$input.RepAlu.vcf $outdir$input.nonRep.vcf > $outdir$input.All.vcf ");
