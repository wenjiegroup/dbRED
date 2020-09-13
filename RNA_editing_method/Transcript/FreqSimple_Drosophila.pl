use strict;

if (@ARGV != 1){
	die "need to provide 1 input: name\n";
}

my $input = $ARGV[0];

my $bedtools = "/home/lihao/bin/RNA_editing_method/Transcript/BEDTools/bin/intersectBed";
my $simple = "/home/lihao/bin/RNA_editing_method/Transcript/simple_repeats_melanogaster.txt";

open (f1,"$input.blat.vcf") || die "Error $input.blat.vcf";
open (o1,">$input.blat.temp") || die "Error";
while (<f1>)
{
	$_=~s/\s+$//;
	my @a = split /\t/,$_;
	if ($a[5] > 0.1){print o1 "$a[0]\t$a[1]\t$a[1]\t$a[2]\t$a[3]\t$a[4]\t$a[5]\n";}
}
close f1;
close o1;

my $command = "$bedtools -a $input.blat.temp -b $simple -v > $input.blat.temp2";
system ("$command");
open (f1,"$input.blat.temp2") || die "Error";
open (o1,">$input.sim.vcf") || die "error";
while (<f1>)
{
	my @a = split /\t/,$_;
	print o1 "$a[0]\t$a[1]\t$a[3]\t$a[4]\t$a[5]\t$a[6]";
}
close f1;
close o1;
system "rm $input.blat.temp";
system "rm $input.blat.temp2";