import os
import sys

project = sys.argv[1]

f = open(project+'_strand_alt_ref_result','r')
fout = open(project+'.avinput', 'w')
for line in f.readlines():
    line = line.split()
    fout.write(line[0] + '\t' + line[1] + '\t' + line[1]  + '\t' + line[4] + '\t' + line[3] + '\n')
fout.close()
f.close()
