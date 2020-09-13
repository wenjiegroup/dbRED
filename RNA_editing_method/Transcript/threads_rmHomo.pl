use strict;
use threads;
use threads::shared;

my $file = $ARGV[0];
my $outfile = $ARGV[0];
my $process = $ARGV[1];

my $PerlScript="/public2/home/zhaoch/RNA_editing_script_for_Zhaochenghui/RNA_editing_method/Transcript/RemoveHomoNucleotides.pl";
my $outdir="_rmHomoFiles";
if(!(-e "$file$outdir")){mkdir "$file$outdir";}

open(f1,"$file.sj.vcf")||die"error open $file.sj.vcf\n ";
my $totalsite;
while(<f1>){$totalsite++;}
close f1;
my $eachNum=int($totalsite/$process)+1;

my $j=0;
my $thread;
while(1)
{
	last if ($j >= $process);
	while( scalar(threads->list()) < $process)
	{
		$j++;
		my $params = join "\t",$file,$j;
		threads -> new(\&rmHomo,$params);
	}
	foreach $thread(threads->list(threads::all))
	{
		if($thread->is_joinable())
		{
			$thread->join();
		}
	}
}

foreach $thread(threads->list(threads::all)){$thread->join();}

open(o1,">$outfile.homo.vcf")||die"error";
for(my$i=1;$i<=$process;$i++)
{
	open (f1,"$file$outdir/sj.TMP$i") || die "Error";
	while (<f1>){print o1 "$_";}
	close f1;
}

sub rmHomo()
{
	my $params = shift;
	my ($input,$i) = split /\t/,$params;
	print "TMP$i\n";
	open (f1,"$input.sj.vcf") || die "Error";
	open (o1,">$file$outdir/sj.$i.vcf") || die "Error $file$outdir/sj.$i.vcf";
	my $num = 0;
	my $n;
	while (<f1>)
	{
		if ($num < ($i)*$eachNum && $num >= ($i-1)*$eachNum)
		{$n++;print o1 "$_";}
		$num++;
	}
	close f1;
	close o1;
	system "perl $PerlScript $file$outdir/sj.$i.vcf $file$outdir/sj.TMP$i";
}
