use warnings;
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
	my ($chrom, $pos, $ref, $mut, $qual) = ($fields[0], $fields[1], $fields[3], $fields[4], $fields[5]);
	
	#if ($chrom eq "chrM" || length($chrom) > 5){next;}
	my ($refnum, $mutnum, $varfreq);
	
	for (my $i = 9;$i < scalar(@fields);$i++){
		my $info = $fields[$i];
		if ($info eq "./."){next;}
		my @splitinfo = split(/\:/, $info);
		my @nucnums = split(/\,/, $splitinfo[1]);
		($refnum, $mutnum) = ($refnum+$nucnums[0], $mutnum+$nucnums[1]);
	}
	my $totalnum = $refnum + $mutnum;
	$varfreq = sprintf("%.3f",$mutnum/$totalnum);
	if ($varfreq>0.1){print $OUTPUT "$chrom\t$pos\t$totalnum,$mutnum,$qual\t$ref\t$mut\t$varfreq\n";} 		
}
close $INPUT;
close $OUTPUT;
