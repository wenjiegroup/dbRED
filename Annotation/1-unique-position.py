#coding: utf-8
#merge A-to-I editing sites from four identification methods
#S:Jinbilly_single P:Jinbilly_pool D:Deepred G:Giremi
import os
import sys

base_dir = '/public2/home/zhaoch/'
project = sys.argv[1]
cutoff = sys.argv[2]
celllines = os.listdir(base_dir+project)
print celllines

RnaEdits = {}

def readRnaEdits(filename, method):
    try:
        with open(filename,'r') as f:
            for line in f.readlines():
                line = line.strip().split('\t')
                chr = line[0]
                if 'chr' not in chr:
                   chr = 'chr' + chr
                position = int(line[1])
                if chr not in RnaEdits:
                    RnaEdits[chr] = {}
                    RnaEdits[chr][position] = method
                else:
                    if position not in RnaEdits[chr]:
                        RnaEdits[chr][position] = method
                    else:
                        if method not in RnaEdits[chr][position]:
                            RnaEdits[chr][position] += method
    except IOError:
        print "The file "+filename+"doesn't exist...."

for cellline in celllines:
    cellline_dir = base_dir + project +'/' + cellline + '/'
    #Jinbilly_single
    Jinbilly_single_samples = os.listdir(cellline_dir + 'Jinbilly_single')
    print Jinbilly_single_samples
    for Jinbilly_single_sample in Jinbilly_single_samples:
        readRnaEdits(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.AtoI.filter.vcf', 'S')


    #Jinbilly_pool
    readRnaEdits(cellline_dir + 'Jinbilly_pool/' + cellline + '.AtoI.filter.vcf', 'P')

    #Giremi
    Giremi_samples = os.listdir(cellline_dir + 'Giremi')
    for Giremi_sample in Giremi_samples:
        readRnaEdits(cellline_dir+'Giremi'+'/'+Giremi_sample+'/'+Giremi_sample+'.GIREMI.AtoIediting.txt', 'G')

    #Deepred
    for DeepRed_sample in Jinbilly_single_samples:
        readRnaEdits(cellline_dir+'DeepRed'+'/'+DeepRed_sample+'.AtoI.gene.cutoff_'+cutoff+'.txt', 'D')

#output the unique result
fout = open(project+'_final_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + final_pos_method[1] + '\n')
