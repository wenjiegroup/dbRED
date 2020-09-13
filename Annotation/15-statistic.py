#coding:utf-8
#collect the editing levels from multiple samples

import os
import sys

base_dir = '/public2/home/zhaoch/'
annovar_dir = '/public2/home/zhaoch/annovar/'
project = sys.argv[1]

files = os.listdir(annovar_dir+project)

RnaEdits = {}
def readRnaEdits(filename):
    try:
        with open(filename,'r') as f:
            for line in f.readlines():
                line = line.strip().split('\t')
                chr = line[0]
                # if 'chr' not in chr:
                #     chr = 'chr' + chr
                position = int(line[1])
                method = line[2]
                if chr not in RnaEdits:
                    RnaEdits[chr] = {}
                    RnaEdits[chr][position] = method
                else:
                    if position not in RnaEdits[chr]:
                        RnaEdits[chr][position] = method
                    else:
                        RnaEdits[chr][position] += ' '+method
    except IOError:
        print "The file "+filename+"doesn't exist...."

for file in files:
    readRnaEdits(annovar_dir+project+'/'+file)

#output the unique result
fout = open(project+'_editing_level', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + final_pos_method[1] + '\n')

# total_num = 0
# single_num = 0
# one_num = 0
# for file in files:
#     with open(annovar_dir+project+'/'+file, 'r') as f:
#         for line in f.readlines():
#             line = line.strip().split('\t')
#             level = line[2]
#             level = level.split(' ')
#             if len(level) == 1:
#                 single_num += 1
#                 if float(level[0]) == 1.0:
#                     one_num += 1
#             total_num += 1
# print 'total_num', total_num
# print 'single_num', single_num
# print 'one_num', one_num
