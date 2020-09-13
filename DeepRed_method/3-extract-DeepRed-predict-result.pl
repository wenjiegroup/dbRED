use strict;


my $order="./Raw_Data/$ARGV[0]_for_Input_Data_chr/order_of_location.$ARGV[1].txt";#$ARGV[0]: your project name;$ARGV[1]: sampleID
my $score="./Score/Score_combined/$ARGV[0]_for_Input_Data_chr/Score_predicted.$ARGV[1].txt";
my $output="./Predict_result/$ARGV[0]_for_Input_Data_chr/predict_of_result_$ARGV[1].txt";
my $gatk="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[1]/$ARGV[1].gatk.vcf";
my $con="/public2/home/zhaoch/STAR_mapping_dir/$ARGV[1]/$ARGV[1].con.vcf";
my $result="./Predict_result/$ARGV[0]_for_Input_Data_chr/$ARGV[1].DeepRed.txt";
my $script="RNA_editing_method/Transcript";
my @a;
my %site;
my $key;
my $dir="./Predict_result/$ARGV[0]_for_Input_Data_chr";
if(!(-e $dir)){mkdir $dir or die};
system("paste $order $score > $output");
system("perl $script/Convert_VCF.pl $gatk $con");
open(f,$con)||die"error $con\n";
while(<f>)
{
	@a = split/\s+/,$_;
	$site{$a[0]."\t".$a[1]}=join"\t",@a[2..@a-1];
}
close f;

open(o,">$result")||die"error $result\n";
open(f,$output)||die"error open $output\n";
while(<f>)
{
	@a = split/\s+/,$_;
	$key=$a[0]."\t".$a[1];
	if(exists $site{$key})
	{
		print o $a[0]."\t".$a[1]."\t".$site{$key}."\t".$a[2]."\n";
	}
}
close f;
close o;





