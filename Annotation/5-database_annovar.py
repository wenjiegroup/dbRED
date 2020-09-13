#coding:utf-8
#record whether the editing sites exist in known databases
#D：Darned A(P)：RedIpotal R：Radar E:dbRed

import os
import sys

project = sys.argv[1]
RnaEdits = {}

Rdict = []
Pdict = []
Ddict = []

with open('database/Darned.txt', 'r') as f:
    for line in f.readlines():
        line = line.split('\t')
        Ddict.append(line[0]+':'+line[1])

with open('database/Radar.txt', 'r') as f:
    for line in f.readlines():
        line = line.split('\t')
        Rdict.append(line[0]+':'+line[1])

with open('database/RedIpotal.txt', 'r') as f:
    for line in f.readlines():
        line = line.split('\t')
        Pdict.append(line[0]+':'+line[1])

# with open('database/RADAR_RNA_editing_database/Mouse_AG_all_mm9_liftover_mm10_v2.bed', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         Rdict.append(line[0]+':'+line[1])
#
# with open('database/RADAR_RNA_editing_database/Mouse_AG_all_mm9_v2.bed', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         Rdict.append(line[0]+':'+line[1])
#
# with open('database/RADAR_RNA_editing_database/Mouse_AG_all_mm9_v2.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         Rdict.append(line[0]+':'+line[1])
#
# with open('database/DARNED_RNA_editing_database/mm10.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         Ddict.append(line[0]+':'+line[1])

# with open('database/DARNED_RNA_editing_database/dm3.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         Ddict.append(line[0]+':'+line[1])
#
# with open('database/RADAR_RNA_editing_database/Fly_AG_all_dm3_v2.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         Rdict.append(line[0]+':'+line[1])

Rdict = set(Rdict)
Pdict = set(Pdict)
Ddict = set(Ddict)

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

def annovar_database(database_dict, database_name):
    for chr in RnaEdits.keys():
        for position in RnaEdits[chr].keys():
            if chr+':'+str(position) in database_dict:
                RnaEdits[chr][position] += database_name

annovar_database(Rdict, 'R')
annovar_database(Pdict, 'P')
annovar_database(Ddict, 'D')

#output the unique result
fout = open(project+'_database_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + final_pos_method[1] + '\n')
