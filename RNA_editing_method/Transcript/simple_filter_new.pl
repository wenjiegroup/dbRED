use warnings;
use strict;

if (@ARGV != 2) {
	die "need to provide 2 inputs: shared variant file and outputfile name\n";
}
my ($inputfile, $outputfile) = @ARGV;
my $bedtools = "./software/BEDTools/bin/intersectBed";
my $simple = "./Transcript/simple_repeats.txt";

############### Step 1 : transfer #################
open (f1,"$inputfile") || die "error";
open (o1,">$inputfile.temp") || die "error";
while (<f1>)
{my @a = split /\t/,$_;print o1 "$a[0]\t$a[1]\t$a[1]\t$a[2]\t$a[3]\t$a[4]\t$a[7]";}
close f1;
close o1;
############### Step 2 : bedtools ###################
my $command = "$bedtools -a $inputfile.temp -b $simple -v > $outputfile.temp";
system ("$command");
my %hash;
open (f1,"$outputfile.temp") || die "Error";
open (o1,">$outputfile") || die "error";
while (<f1>)
{
	my @a = split /\t/,$_;
	my $b = join "\t",$a[0],$a[1];
	if ($hash{$b} eq "")
	{
		print o1 "$a[0]\t$a[1]\t$a[3]\t$a[4]\t$a[5]\t$a[6]";
		$hash{$b} = 1;
	}
}
close f1;
close o1;
system "rm $inputfile.temp";
system "rm $outputfile.temp";