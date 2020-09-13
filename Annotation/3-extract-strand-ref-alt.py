#coding: utf-8
#record the information of strand and alt-ref bases.
import os
import sys

base_dir = '/public2/home/zhaoch/'
project = sys.argv[1]
celllines = os.listdir(base_dir+project)
print celllines

RnaEdits = {}

def readRnaEdits(filename, strand_pos, ref_pos, alt_pos):
    try:
        with open(filename,'r') as f:
            for line in f.readlines():
                line = line.strip().split('\t')
                chr = line[0]
                if 'chr' not in chr:
                   chr = 'chr' + chr
                position = int(line[1])
                strand = line[strand_pos]
                alt = line[alt_pos]
                ref = line[ref_pos]
                record = strand + ' '+alt+' '+ref
                if chr not in RnaEdits:
                    RnaEdits[chr] = {}
                    RnaEdits[chr][position] = record
                else:
                    if position not in RnaEdits[chr]:
                        RnaEdits[chr][position] = record
    except IOError:
        print "The file "+filename+"doesn't exist...."

for cellline in celllines:
    cellline_dir = base_dir + project +'/' + cellline + '/'
    #Jinbilly_single
    Jinbilly_single_samples = os.listdir(cellline_dir + 'Jinbilly_single')
    print Jinbilly_single_samples
    for Jinbilly_single_sample in Jinbilly_single_samples:
        readRnaEdits(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.AtoI.filter.vcf', -1, 3, 4)
        #readRnaEdits(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.Allfilter.vcf', -1, 3, 4)

    #Jinbilly_pool
    readRnaEdits(cellline_dir + 'Jinbilly_pool/' + cellline + '.AtoI.filter.vcf', -1, 3, 4)
    #readRnaEdits(cellline_dir + 'Jinbilly_pool/' + cellline + '.Allfilter.vcf', -1, 3, 4)

    #Giremi
    Giremi_samples = os.listdir(cellline_dir + 'Giremi')
    for Giremi_sample in Giremi_samples:
        readRnaEdits(cellline_dir+'Giremi'+'/'+Giremi_sample+'/'+Giremi_sample+'.GIREMI.AtoIediting.txt', 2, 3, 4)
        # if cellline == 'HepG2':
        #     readRnaEdits(cellline_dir+'Giremi'+'/'+Giremi_sample+'/'+Giremi_sample+'.GIREMI.RNAediting.filter.txt', 2, 2, 3)
        # else:
        #     readRnaEdits(cellline_dir+'Giremi'+'/'+Giremi_sample+'/'+Giremi_sample+'.GIREMI.RNAediting.filter.txt', 2, 3, 4)

    #Deepred
    for DeepRed_sample in Jinbilly_single_samples:
        readRnaEdits(cellline_dir+'DeepRed'+'/'+DeepRed_sample+'.AtoI.gene.cutoff_0.45.txt', -1, 3, 4)
        #readRnaEdits(cellline_dir+'DeepRed'+'/'+Jinbilly_single_sample+'.Allfilter.cutoff_0.45.txt', -1, 3, 4)
#output
fout = open(project+'_strand_alt_ref_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + ' ' + str(final_pos_method[0]) + ' ' + final_pos_method[1] + '\n')
