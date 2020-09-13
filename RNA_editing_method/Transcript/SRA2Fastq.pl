use strict;

my $dir = "./SRP020490";
opendir (DIR,"$dir") || die "error";
my @file = readdir (DIR);
closedir (DIR);
my $m;
my $outdir = "./SRP020490_fastq/";
foreach $m(@file)
{
	if ($m eq "." || $m eq ".."){next;}
	my @name = split /\.sra/,$m;
	print "$m\n";
	my $command = "/public3/liufeng/Software/sratoolkit/sratoolkit.2.3.1-ubuntu64/bin/fastq-dump --dumpbase -O $outdir$name[0]_fastq $dir/$m";  ### for linux
	system ("$command");
}