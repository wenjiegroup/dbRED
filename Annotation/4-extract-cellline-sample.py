#coding: utf-8
#record the sample and cell line information
#strand-alt-ref
import os
import sys

base_dir = '/public2/home/zhaoch/'
project = sys.argv[1]
celllines = os.listdir(base_dir+project)
print celllines

RnaEdits = {}

def readRnaEdits(filename, cellline, sample=None):
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
                    RnaEdits[chr][position] = {}
                    RnaEdits[chr][position]['cellline'] = [cellline]
                    RnaEdits[chr][position]['sample'] = [sample]
                else:
                    if position not in RnaEdits[chr]:
                        RnaEdits[chr][position] = {}
                        RnaEdits[chr][position]['cellline'] = [cellline]
                        RnaEdits[chr][position]['sample'] = [sample]
                    else:
                        RnaEdits[chr][position]['cellline'].append(cellline)
                        RnaEdits[chr][position]['sample'].append(sample)
    except IOError:
        print "The file "+filename+" doesn't exist...."

for cellline in celllines:
    cellline_dir = base_dir + project +'/' + cellline + '/'
    #Jinbilly_single
    Jinbilly_single_samples = os.listdir(cellline_dir + 'Jinbilly_single')
    print Jinbilly_single_samples
    for Jinbilly_single_sample in Jinbilly_single_samples:
        readRnaEdits(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.AtoI.filter.vcf', cellline, Jinbilly_single_sample)

    #Jinbilly_pool
    readRnaEdits(cellline_dir + 'Jinbilly_pool/' + cellline + '.AtoI.filter.vcf', cellline)

    #Giremi
    Giremi_samples = os.listdir(cellline_dir + 'Giremi')
    for Giremi_sample in Giremi_samples:
        readRnaEdits(cellline_dir+'Giremi'+'/'+Giremi_sample+'/'+Giremi_sample+'.GIREMI.AtoIediting.txt', cellline, Giremi_sample)

    #Deepred
    for DeepRed_sample in Jinbilly_single_samples:
        readRnaEdits(cellline_dir+'DeepRed'+'/'+DeepRed_sample+'.AtoI.gene.cutoff_0.95.txt', cellline, DeepRed_sample)


fout = open(project+'_cellline_sample_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t')
        for cellline in set(final_pos_method[1]['cellline']):
            fout.write(cellline+';')
        fout.write('\t')
        for sample in set(final_pos_method[1]['sample']):
            if sample != None:
                fout.write(sample+';')
        fout.write('\n')
