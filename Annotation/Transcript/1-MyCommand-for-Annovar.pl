use strict;
my $input=$ARGV[0];#"./ERR188021.All.vcf";
my $annovar="/public2/home/zhaoch/local/annovar";
my $output=$ARGV[1];#"./ERR188021";
my @a;
my %anno;

open(o,">$output.avinput")||die"error $input.avinput\n";
open(f,$input)||die"error open $input\n";
while(<f>)
{
	@a = split/\s+/,$_;
	my $k=join"\t",($a[0],$a[1],$a[1],$a[3],$a[4]);
	print o "$k\n";
}
close f;
close o;

system("perl $annovar/annotate_variation.pl -buildver hg19 -dbtype wgEncodeGencodeBasicV24lift37 --outfile $output $output.avinput $annovar/humandb/");

open(f,"$output.variant_function")||die"error open $output.variant_function\n";
while(<f>)
{
	@a= split/\s+/,$_;
	$anno{$a[2]."\t".$a[3]}=$a[5]."\t".$a[6]."\t".$a[0]."\t".$a[1];
}
close f;

open(f,"$output.exonic_variant_function")||die"error $output.exonic_variant_function\n";
while(<f>)
{
	chomp $_;
	@a= split/\t/,$_;
	$anno{$a[3]."\t".$a[4]}=$a[6]."\t".$a[7]."\t".$a[1]."\t".$a[2];
}
close f;

open(o,">$output.finalAnno.txt")||die"error $output.finalAnno.txt\n";
open(f,"$output.avinput")||"error open $output.avinput\n";
while(<f>)
{
	@a= split/\s+/,$_;
	print o $a[0]."\t".$a[1]."\t".$anno{$a[0]."\t".$a[1]}."\n";
}
close f;
close o;
=cut;
foreach my $i (sort keys %anno)
{
	print o $i."\t".$anno{$i}."\n";
}
close o;
=cut;




