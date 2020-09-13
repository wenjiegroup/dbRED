#coding:utf-8
#whether editing sites is in dbsnp

import os
import sys

project = sys.argv[1]
RnaEdits = {}

dbsnp_dict = {}

with open('/public2/home/zhaoch/Reference_data/dbsnp_137.hg19.vcf', 'r') as f:
    for line in f.readlines():
        if line[0] == '#':
            continue
        line = line.split('\t')
        if line[0] not in dbsnp_dict:
            dbsnp_dict[line[0]] = {}
            dbsnp_dict[line[0]][int(line[1])] = line[2]
        else:
            if int(line[1]) not in dbsnp_dict[line[0]]:
                dbsnp_dict[line[0]][int(line[1])] = line[2]

print 'finish reading file'

try:
    with open(project+'_final_result','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            chr = line[0]
            position = int(line[1])
            if chr not in RnaEdits:
                RnaEdits[chr] = {}
                RnaEdits[chr][position] = ''
            else:
                if position not in RnaEdits[chr]:
                    RnaEdits[chr][position] = ''

except IOError:
    print "The file "+filename+"doesn't exist...."

for chr in RnaEdits.keys():
    if chr not in dbsnp_dict.keys():
        continue
    for position in RnaEdits[chr]:
        print chr+':'+str(position)
        #if position in dbsnp_dict[chr]:
        if dbsnp_dict[chr].get(position) != None:
            RnaEdits[chr][position] = dbsnp_dict[chr][position]

#output the unique result
fout = open(project+'_dbsnp_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + final_pos_method[1] + '\n')
