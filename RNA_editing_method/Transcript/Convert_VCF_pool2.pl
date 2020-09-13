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
	my ($chrom, $pos, $ref, $mut, $qual, $info,$info2) = ($fields[0], $fields[1], $fields[3], $fields[4], $fields[5], $fields[9],$fields[10]);
	my @splitinfo = split(/\:/, $info);
	my @splitinfo2 = split(/\:/, $info2);
#	print "$splitinfo[1]\t$splitinfo2[1]\t$splitinfo3[1]\t$splitinfo4[1]\n";
	my @nucnums = split(/\,/, $splitinfo[1]);
	my $len1 = scalar(@nucnums);
	my @nucnums2 = split(/\,/, $splitinfo2[1]);
	my $len2 = scalar(@nucnums2);
		

	my ($refnum1,$mutnum1,$totalnum1,$varfreq1) = (0,0,0,0);
	my ($refnum2,$mutnum2,$totalnum2,$varfreq2) = (0,0,0,0);
	if (length($mut) == 1){
	if ($len1 > 1 or $len2 > 1)
	{
		if ($len1 > 1)
		{($refnum1, $mutnum1) = ($nucnums[0], $nucnums[1]);
		$totalnum1 = $refnum1 + $mutnum1;
		$varfreq1 = sprintf("%.3f",$mutnum1/$totalnum1);}
	
		if ($len2 > 1)
		{($refnum2, $mutnum2) = ($nucnums2[0], $nucnums2[1]);
		$totalnum2 = $refnum2 + $mutnum2;
		$varfreq2 = sprintf("%.3f",$mutnum2/$totalnum2);}
		
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
		if ($varfreq != 0 && $chrom !~ /chrM/ && length($chrom) < 6 && $chrom !~ /chrY/)
		{print $OUTPUT "$chrom\t$pos\t$totalnum,$mutnum,$qual\t$ref\t$mut\t$varfreq\n";} 
	}		}
}
close $INPUT;
close $OUTPUT;
