use warnings;
use strict;

if (@ARGV != 2)
{
	die "need to provide 2 input : inputname and output\n";
}
my $inputfile = $ARGV[0];
my $outputfile = $ARGV[1];
open (f1,"$inputfile") || die "error";
open (o1,">$outputfile") || die "error";

my @a;
while (<f1>)
{
	$_ =~ s/\s+$//;
	@a = split /\t/,$_;
#	print "$a[12]\t$a[13]\n";
	if ($a[13] >= 0.1 and $a[11] >= 3)
	{
		print o1 "$a[0]\t$a[1]\t$a[2]\t$a[3]\t$a[4]\t$a[11]\t$a[12]\t$a[13]\n";
#		print "$a[11]\t$a[12]\t$a[13]\n";
	}
}
close f1;