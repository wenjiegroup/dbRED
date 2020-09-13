use warnings;
use strict;

if (@ARGV != 2) {
	die "need to provide 2 inputs: input sam file and outputfile name\n";
}
my ($inputfile, $outputfile) = @ARGV;

open (f1,"$inputfile") || die "Error";
open (o1,">$outputfile") || die "Error";



my $swich = 0;
my $number;
while (<f1>)
{
	my $@a= split /\t/,$_;
	if ($switch == 0){print o1 "$_";}