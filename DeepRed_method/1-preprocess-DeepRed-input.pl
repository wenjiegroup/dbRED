use strict;

my $time_start=$^T;


my $script="Codes_of_DeepRed";# directory of your downloaded DeepRed code

my $inputName=$ARGV[0];


system("perl $script/A1_check_and_extract_input_data_chr.pl $inputName");
system("matlab  -nodesktop -nosplash -nodisplay -r \"A2_load_data_chr(100,'$inputName\_for_Input_Data_chr');exit\"");

my $time_end=time();
my $time=$time_end-$time_start;
print "start:$time_start\n";
print "end:$time_end\n"; 
print "use_time:$time\n";


