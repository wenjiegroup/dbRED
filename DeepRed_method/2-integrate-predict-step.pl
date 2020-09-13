use strict;

my $time_start=$^T;


my $script="Codes_of_DeepRed";## directory of your downloaded DeepRed code
my $inputName=$ARGV[0];

system("perl $script/C1_run_pbs_of_predicting1_repeatedly.pl $inputName\_for_Input_Data_chr");
system("perl $script/C2_run_pbs_of_predicting2_repeatedly.pl $inputName\_for_Input_Data_chr");
system("perl $script/C3_run_pbs_of_predicting3_repeatedly.pl $inputName\_for_Input_Data_chr");
system("perl $script/C4_run_pbs_of_predicting4_repeatedly.pl $inputName\_for_Input_Data_chr");
my $time_end=time();
my $time=$time_end-$time_start;
print "start:$time_start\n";
print "end:$time_end\n"; 
print "use_time:$time\n";


