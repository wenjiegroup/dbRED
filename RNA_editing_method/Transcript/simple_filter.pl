use warnings;
use strict;

if (@ARGV != 2) {
	die "need to provide 2 inputs: shared variant file and outputfile name\n";
}
my ($inputfile, $outputfile) = @ARGV;

open f1,"/public3/lih/my_work/vcf_index/filter/simple_repeats.txt";
open (INPUT, "<", $inputfile) || die "error";
open (OUTPUT, ">", $outputfile) || die "error";


my %genehash;
while (<f1>)
{
	chomp;
	my @fields = split;
	my $chr = $fields[0];
	push(@{$genehash{$chr}},$_);
}
close f1;

while (<INPUT>)
{
	chomp;
	my $line = $_;
	my @fields = split (/\t/);
	my ($chrom,$position,$found,$chromfound,$splice) = ($fields[0],$fields[1],0,0,0);
	foreach my $geneline (@{$genehash{$chrom}})
	{
		my @fieldsref = split (/\t/,$geneline);
		my ($chromref,$txstart,$txend) = ($fieldsref[0],$fieldsref[1],$fieldsref[2]);
		$splice = 1 if ($txstart-1 < $position and $txend +1 > $position);
	}
	print OUTPUT "$line\n" if ($splice == 0);
}
close INPUT;
close OUTPUT;