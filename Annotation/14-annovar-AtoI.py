#coding: utf-8
#extract A-to-I sites

import os
import sys

base_dir = '/public2/home/zhaoch/'
project = sys.argv[1]

f = open(project+'_strand_alt_ref_result','r')
fout = open(project+'.tmp1', 'w')
for line in f.readlines():
    line = line.split()
    fout.write(line[0] + '\t' + line[1] + '\t' + line[1] + '\t' + line[3] + '\t' + line[4] + '\n')
fout.close()
f.close()

os.system('intersectBed -a '+project+'.tmp1 -b /public2/home/zhaoch/Reference_data/gencode.v25lift37.annotation.gtf.geneInterval -wb > '+project+'.tmp2')

f = open(project+'.tmp2', 'r')
fout = open(project+'.AtoI', 'w')
for line in f.readlines():
    line = line.split()
    if (line[3] == 'A' and line[4] == 'G' and line[8] == '+') or (line[3] == 'T' and line[4] == 'C' and line[8] == '-'):
        fout.write(line[0] + '\t' + line[1] + '\t' + line[3] + '\t' + line[4] + '\t' + line[8] + '\n')
fout.close()
f.close()
