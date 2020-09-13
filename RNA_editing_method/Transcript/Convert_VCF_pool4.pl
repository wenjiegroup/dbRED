#use warnings;
use strict;

if (@ARGV != 2) {
	die "need to provide 2 inputs: shared variant file and outputfile name\n";
}

my ($inputfile, $outputfile) = @ARGV;

open (my $INPUT, "<", $inputfile);
open (my $OUTPUT, ">", $outputfile);
#print $OUTPUT "chrom\tpos\ttotalnum,mutnum,qual\tref\tmut\tvarfreq\n";
while(<$INPUT>) {
	chomp;
	my $line = $_;
	next if ($line =~ m/^\#/);
	my @fields = split;
	my ($chrom, $pos, $ref, $mut, $qual, $info,$info2,$info3,$info4) = ($fields[0], $fields[1], $fields[3], $fields[4], $fields[5], $fields[9],$fields[10],$fields[11],$fields[12]);
	my @splitinfo = split(/\:/, $info);
	my @splitinfo2 = split(/\:/, $info2);
	my @splitinfo3 = split(/\:/, $info3);
	my @splitinfo4 = split(/\:/, $info4);
#	print "$splitinfo[1]\t$splitinfo2[1]\t$splitinfo3[1]\t$splitinfo4[1]\n";
	my @nucnums = split(/\,/, $splitinfo[1]);
	my $len1 = scalar(@nucnums);
	my @nucnums2 = split(/\,/, $splitinfo2[1]);
	my $len2 = scalar(@nucnums2);
	my @nucnums3 = split(/\,/, $splitinfo3[1]);
	my $len3 = scalar(@nucnums3);
	my @nucnums4 = split(/\,/, $splitinfo4[1]);
	my $len4 = scalar(@nucnums4);
		

	my ($refnum1,$mutnum1,$totalnum1,$varfreq1) = (0,0,0,0);
	my ($refnum2,$mutnum2,$totalnum2,$varfreq2) = (0,0,0,0);
	my ($refnum3,$mutnum3,$totalnum3,$varfreq3) = (0,0,0,0);
	my ($refnum4,$mutnum4,$totalnum4,$varfreq4) = (0,0,0,0);
	if (length($mut) == 1){
	if (($len1 > 1 and $len2 > 1) or ($len3 > 1 and $len4 > 1))
	{
		if ($len1 > 1)
		{($refnum1, $mutnum1) = ($nucnums[0], $nucnums[1]);
		$totalnum1 = $refnum1 + $mutnum1;
		$varfreq1 = sprintf("%.3f",$mutnum1/$totalnum1);}
	
		if ($len2 > 1)
		{($refnum2, $mutnum2) = ($nucnums2[0], $nucnums2[1]);
		$totalnum2 = $refnum2 + $mutnum2;
		$varfreq2 = sprintf("%.3f",$mutnum2/$totalnum2);}
		
		if ($len3 > 1)
		{($refnum3, $mutnum3) = ($nucnums3[0], $nucnums3[1]);
		$totalnum3 = $refnum3 + $mutnum3;
		$varfreq3 = sprintf("%.3f",$mutnum3/$totalnum3);}
		
		if ($len4 > 1)
		{($refnum4, $mutnum4) = ($nucnums4[0], $nucnums4[1]);
		$totalnum4 = $refnum4 + $mutnum4;
		$varfreq4 = sprintf("%.3f",$mutnum4/$totalnum4);}
		
		my ($totalnum,$mutnum);
		my $varfreq = 2;
		if ($varfreq > $varfreq1 and $len1 > 1)
		{
			$varfreq = $varfreq1;
			$totalnum = $totalnum1;
			$mutnum = $mutnum1;
		}
	 	if ($varfreq > $varfreq2 and $len2 > 1) 
		{
			$varfreq = $varfreq2;
			$totalnum = $totalnum2;
			$mutnum = $mutnum2;
		}
		if ($varfreq > $varfreq3 and $len3 > 1) 
		{
			$varfreq = $varfreq3;
			$totalnum = $totalnum3;
			$mutnum = $mutnum3;
		}
		if ($varfreq > $varfreq4 and $len4 > 1) 
		{
			$varfreq = $varfreq4;
			$totalnum = $totalnum4;
			$mutnum = $mutnum4;
		}
		if ($varfreq != 0 && $chrom !~ /chrM/ && length($chrom) < 6 && $chrom !~ /chrY/)
		{print $OUTPUT "$chrom\t$pos\t$totalnum,$mutnum,$qual\t$ref\t$mut\t$varfreq\n";} 
	}		}
}
close $INPUT;
close $OUTPUT;
