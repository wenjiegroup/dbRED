use strict;

if (@ARGV != 1){
	die "need to provide 1 input:name\n";
}
my ($inputfile) = ($ARGV[0]);
open (f1,"$inputfile.gatk.raw.vcf") || die "error";
open (f2,"$inputfile.nonAlu.vcf") || die "error";
open (o1,">$inputfile.GatkTononAlu.vcf") || die "error";

my @a;
my $location;
my %info;
while (<f1>)
{
	#print "read gatk file\n";
	$_ =~ s/\s+$//;
	@a = split /\t/,$_;
	if ($a[0] !~ /#/ < 6 and length($a[4]) == 1)
	{	
		$location = join "-",$a[0],$a[1];
		my ($info1,$info2,$info3,$info4) = ($a[9],$a[10],$a[11],$a[12]);
		my @splitinfo1 = split(/\:/, $info1);
		my @splitinfo2 = split(/\:/, $info2);
		my @splitinfo3 = split(/\:/, $info3);
		my @splitinfo4 = split(/\:/, $info4);

		my $refnum = 0;
		my $mutnum = 0;
		$totalnum = $refnum + $mutnum;
		if (scalar(@splitinfo1) > 1)
		{
			my @nucnums1 = split(/\,/, $splitinfo1[1]);
			$refnum = $refnum + $nucnums1[0];
			$mutnum = $mutnum + $nucnums1[1];
			$info{$location} = join "\t",$info{$location},$splitinfo1[1];
		}
		else 
		{
			$info{$location} = join "\t",$info{$location},$splitinfo1[0];
		}
		if (scalar(@splitinfo2) > 1)
		{
			my @nucnums2 = split(/\,/, $splitinfo2[1]);
			$refnum = $refnum + $nucnums2[0];
			$mutnum = $mutnum + $nucnums2[1];
			$info{$location} = join "\t",$info{$location},$splitinfo2[1];
		}
		else 
		{
			$info{$location} = join "\t",$info{$location},$splitinfo2[0];
		}
		if (scalar(@splitinfo3) > 1)
		{
			my @nucnums3 = split(/\,/, $splitinfo3[1]);
			$refnum = $refnum + $nucnums3[0];
			$mutnum = $mutnum + $nucnums3[1];
			$info{$location} = join "\t",$info{$location},$splitinfo3[1];
		}
		else 
		{
			$info{$location} = join "\t",$info{$location},$splitinfo3[0];
		}
		if (scalar(@splitinfo4) > 1)
		{
			my @nucnums4 = split(/\,/, $splitinfo4[1]);
			$refnum = $refnum + $nucnums4[0];
			$mutnum = $mutnum + $nucnums4[1];
			$info{$location} = join "\t",$info{$location},$splitinfo4[1];
		}
		else 
		{
			$info{$location} = join "\t",$info{$location},$splitinfo4[0];
		}
		my $totalnum = $refnum + $mutnum;
		my $varfreq = sprintf("%.3f",$mutnum/$totalnum);
		$info{$location} = join "\t",$info{$location},$mutnum,$totalnum,$varfreq;
	#	print "$info{$location}\n";
	}
}
close f1;
while (<f2>)
{
#	print "write file\n";
	$_ =~ s/\s+$//;
	@a = split /\t/,$_;
	$location = join "-",$a[0],$a[1];
	print o1 "$_\t$info{$location}\n";
}
close f2;
close o1;