import os
import sys
project = sys.argv[1]
f = open(project+'_strand_alt_ref_result','r')
fout = open(project+'_unique.bed', 'w')
num = 0
for line in f.readlines():
    line = line.split()
    chr = line[0]
    pos = int(line[1])
    fout.write(chr + '\t' + str(pos-1) + '\t' + str(pos) + '\t' + str(num) + '\n')
    num += 1
fout.close()
f.close()
os.system('perl Transcript/1-bigWig-to-phastcon-with-freq-Human.pl '+project)
