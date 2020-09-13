use strict;
use Cwd;
my $tmp=".";
opendir(DIR, $tmp) || die "Can't open directory $tmp"; 
my @filename = readdir(DIR); 
close DIR;

my $nfile = 0;
my $i;
my $alnout;
my $command;

foreach (@filename) 
{
	$nfile++;
}

my @a;
my $path = getcwd;
for($i=0;$i<$nfile;$i++)
{	
	if(@filename[$i] =~ '.dedup.sam')
	{
		@a = split /.dedup.sam/,@filename[$i];
		$alnout = $a[0];
		
		$command = "java -Xmx4g convertCoordinates < $alnout.dedup.sam > $alnout.java.sam";
		print "$command\n";
		system ("$command");
=cut;
		$command = "rm -rf $a[0].bq.sam";
		print "$command\n";
		system ("$command");
		
		$command = "cp $a[0].java.sam /public6/Lihao/RNA-editting/Long/";
		print "$command\n";
		system ("$command");
		$command = "rm -rf /home/Lihao/$a[0].java.sam .";
		print "$command\n";
		system ("$command");
=cut;
	}
}
