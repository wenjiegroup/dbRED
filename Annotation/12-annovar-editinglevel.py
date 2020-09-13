#coding: utf-8
#extrct the editing levels
import os
import sys

base_dir = '/public2/home/zhaoch/'
annovar_dir = '/public2/home/zhaoch/annovar/'
project = sys.argv[1]
celllines = os.listdir(base_dir+project)

if not os.path.exists(annovar_dir+project):
    os.makedirs(annovar_dir+project)

RnaEditLevel = {}
RnaEdits = {}

def readLevel(filename):
    tmp_RnaEditlevel = {}
    try:
        with open(filename,'r') as f:
            for line in f.readlines():
                line = line.strip().split('\t')
                chr = line[0]
                if 'chr' not in chr:
                    chr = 'chr' + chr
                position = int(line[1])
                level = line[5]
                if chr not in tmp_RnaEditlevel:
                    tmp_RnaEditlevel[chr] = {}
                    tmp_RnaEditlevel[chr][position] = level
                else:
                    if position not in tmp_RnaEditlevel[chr]:
                        tmp_RnaEditlevel[chr][position] = level
        return tmp_RnaEditlevel
    except IOError:
        print filename+" doesn't exist"

def readRnaEdits(filename):
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
                    RnaEdits[chr][position] = ''
                else:
                    if position not in RnaEdits[chr]:
                        RnaEdits[chr][position] = ''
    except IOError:
        print "The file "+filename+" doesn't exist...."

def saveLevel(tmp_level):
    for chr in RnaEdits:
        for position in RnaEdits[chr]:
            #print chr,position
            if chr not in RnaEditLevel:
                RnaEditLevel[chr] = {}
                RnaEditLevel[chr][position] = [tmp_level[chr][position]]
            else:
                #print chr,position,tmp_level[chr][position]
                if position not in tmp_level[chr]:
                    continue
                if position not in RnaEditLevel[chr]:
                    RnaEditLevel[chr][position] = [tmp_level[chr][position]]
                else:
                    RnaEditLevel[chr][position].append(tmp_level[chr][position])

def print_info(tmp_level):
    print("RnaEdits\n")
    for chr in RnaEdits:
        print chr
    print("RnaEdits_level\n")
    for chr in tmp_level:
        print chr

for cellline in celllines:
    print cellline

    cellline_dir = base_dir + project +'/' + cellline + '/'

    
    Jinbilly_single_samples = os.listdir(cellline_dir + 'Jinbilly_single')
    #print Jinbilly_single_samples
    for Jinbilly_single_sample in Jinbilly_single_samples:
        print Jinbilly_single_sample
        single_rnaeditslevel = readLevel(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.con.vcf')
        #Jinbilly_single
        readRnaEdits(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.AtoI.vcf')
        #readRnaEdits(cellline_dir+'Jinbilly_single'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.Allfilter.vcf')
        #Giremi

        readRnaEdits(cellline_dir+'Giremi'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.GIREMI.AtoIediting.txt')
        #readRnaEdits(cellline_dir+'Giremi'+'/'+Jinbilly_single_sample+'/'+Jinbilly_single_sample+'.GIREMI.RNAediting.filter.txt')
        #print 'giremi', RnaEdits['chrX'][73416984]
        #Deepred
        readRnaEdits(cellline_dir+'DeepRed'+'/'+Jinbilly_single_sample+'.AtoI.gene.cutoff_0.95.txt')
        #readRnaEdits(cellline_dir+'DeepRed'+'/'+Jinbilly_single_sample+'.Allfilter.cutoff_0.45.txt')
      
        #print_info(single_rnaeditslevel)
        #print 'deepred', RnaEdits['chrX'][73416984]
        saveLevel(single_rnaeditslevel)
        RnaEdits = {}

    #Jinbilly_pool
    readRnaEdits(cellline_dir + 'Jinbilly_pool/' + cellline + '.AtoI.vcf')
    #readRnaEdits(cellline_dir + 'Jinbilly_pool/' + cellline + '.Allfilter.vcf')
    pool_rnaeditslevel = readLevel(cellline_dir+'Jinbilly_pool'+'/'+ cellline +'.con.vcf')
    saveLevel(pool_rnaeditslevel)
    #output the unique result
    fout = open(annovar_dir+project+'/'+cellline+'_level_result', 'w')
    Sort_RnaEdits = sorted(RnaEditLevel.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t')
            for num in final_pos_method[1]:
                fout.write(num+' ')
            fout.write('\n')
    fout.close()
    RnaEdits = {}
    RnaEditLevel = {}
