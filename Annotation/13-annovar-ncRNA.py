#coding: utf-8
#annotate ncRNA information

import os
import sys

base_dir = '/public2/home/zhaoch/'
ncRNA_dir = '/public2/home/zhaoch/annovar/dbRed_noncode_annotation/'
project = sys.argv[1]
specie = sys.argv[2]

def readRnaEdits(filename):
    try:
        RnaEdits = {}
        with open(filename,'r') as f:
            for line in f.readlines():
                line = line.strip().split('\t')
                chr = line[0]
                # if 'chr' not in chr:
                #     chr = 'chr' + chr
                position = int(line[1])
                if chr not in RnaEdits:
                    RnaEdits[chr] = {}
                    RnaEdits[chr][position] = {}
                else:
                    if position not in RnaEdits[chr]:
                        RnaEdits[chr][position] = {}
        return RnaEdits
    except IOError:
        print "The file "+filename+" doesn't exist...."

def readncRNA(RnaEdits, file, filetype, ncRNA):
    with open(file) as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            chr = line[0]
            position = int(line[1])
            if filetype == 0:
                name = line[7]
            elif filetype == 2:
                if line[5] == 'exon':
                    name = line[11].split(';')[3].split('=')[1]
                else:
                    continue
            elif filetype == 3:
                name = line[11].split(';')[2].split('=')[1]
            elif filetype == 4:
                name = line[6]

            if filetype == 1:
                if ncRNA not in RnaEdits[chr][position]:
                    RnaEdits[chr][position][ncRNA] = ''
            else:
                if ncRNA not in RnaEdits[chr][position]:
                    RnaEdits[chr][position][ncRNA] = name
                else:
                    if name not in RnaEdits[chr][position][ncRNA]:
                        RnaEdits[chr][position][ncRNA] += ';'+name

    return RnaEdits

if specie == 'human':
    os.system('python produce-bed.py '+project)
    fname = project+'.bed'
    circRNA1 = ncRNA_dir + 'circRNA_circBase/hsa_hg19_circRNA.txt'
    circRNA2 = ncRNA_dir + 'circRNA_CSCD/hg19-cancer-circrna.bed'
    circRNA3 = ncRNA_dir + 'circRNA_CSCD/hg19-common-circrna.bed'
    lncRNA = ncRNA_dir + 'lncRNA_gencode/gencode.v27lift37.long_noncoding_RNAs.gff3'
    miRNA = ncRNA_dir + 'miRNA_mirBase/human_hsa.gff3'
    piRNA = ncRNA_dir + 'piRNA_piRBase/piR_hg19_sort.bed'
    #circRNA
    os.system('intersectBed -a ' + fname + ' -b ' + circRNA1 + ' -wb > '+ project +'.tmp1')
    os.system('intersectBed -a ' + fname + ' -b ' + circRNA2 + ' -wb > '+ project +'.tmp2')
    os.system('intersectBed -a ' + fname + ' -b ' + circRNA3 + ' -wb > '+ project +'.tmp3')
    # #lncRNA
    os.system('intersectBed -a ' + fname + ' -b ' + lncRNA + ' -wb > '+ project +'.tmp4')
    # #miRNA
    os.system('intersectBed -a ' + fname + ' -b ' + miRNA + ' -wb > '+ project +'.tmp5')
    # #piRNA
    os.system('intersectBed -a ' + fname + ' -b ' + piRNA + ' -wb > '+ project +'.tmp6')

    RnaEdits = readRnaEdits(project+'.bed')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp1', 0, 'circRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp2', 1, 'circRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp3', 1, 'circRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp4', 2, 'lncRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp5', 3, 'miRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp6', 4, 'piRNA')

    fout = open(project+'_ncRNA', 'w')
    Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        #print type(final[1])
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]))
            for key in final_pos_method[1]:
                fout.write('\t'+key+':'+final_pos_method[1][key])
            fout.write('\n')
    os.system('rm '+project+'.tmp*')

elif specie == 'chim':
    fname = project + '.bed'
    lncRNA = ncRNA_dir + 'lncRNA_noncode/NONCODEv5_panTro4.lncAndGene.bed'
    miRNA = ncRNA_dir + 'miRNA_mirBase/ptn_troglodytes.gff3'
    # #lncRNA
    os.system('intersectBed -a ' + fname + ' -b ' + lncRNA + ' -wb > '+ project +'.tmp4')
    # #miRNA
    os.system('intersectBed -a ' + fname + ' -b ' + miRNA + ' -wb > '+ project +'.tmp5')

    RnaEdits = readRnaEdits(project+'.bed')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp4', 4, 'lncRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp5', 3, 'miRNA')

    fout = open(project+'_ncRNA', 'w')
    Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        #print type(final[1])
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]))
            for key in final_pos_method[1]:
                fout.write('\t'+key+':'+final_pos_method[1][key])
            fout.write('\n')
    os.system('rm '+project+'.tmp*')

elif specie == 'rat':
    fname = project + '.bed'
    lncRNA = ncRNA_dir + 'lncRNA_noncode/NONCODEv5_rn6.lncAndGene.bed'
    miRNA = ncRNA_dir + 'miRNA_mirBase/rat_rno.gff3'
    piRNA = ncRNA_dir + 'piRNA_piRBase/piR_rn4_sort.bed'
    # #lncRNA
    os.system('intersectBed -a ' + fname + ' -b ' + lncRNA + ' -wb > '+ project +'.tmp4')
    # #miRNA
    os.system('intersectBed -a ' + fname + ' -b ' + miRNA + ' -wb > '+ project +'.tmp5')
    # #piRNA
    os.system('intersectBed -a ' + fname + ' -b ' + piRNA + ' -wb > '+ project + '.tmp6')

    RnaEdits = readRnaEdits(project+'.bed')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp4', 4, 'lncRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp5', 3, 'miRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp6', 4, 'piRNA')

    fout = open(project+'_ncRNA', 'w')
    Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        #print type(final[1])
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]))
            for key in final_pos_method[1]:
                fout.write('\t'+key+':'+final_pos_method[1][key])
            fout.write('\n')
    os.system('rm '+project+'.tmp*')

elif specie == 'mouse':
    fname = project + '.bed'
    circRNA = ncRNA_dir + 'circRNA_circBase/mmu_mm9_circRNA.txt'
    lncRNA = ncRNA_dir + 'lncRNA_gencode/gencode.vM16.long_noncoding_RNAs.gff3'
    miRNA = ncRNA_dir + 'miRNA_mirBase/mouse_mmu.gff3'
    piRNA = ncRNA_dir + 'piRNA_piRBase/piR_mouse_s.bed'
    # circRNA
    os.system('intersectBed -a ' + fname + ' -b ' + circRNA + ' -wb > '+ project +'.tmp3')
    # #lncRNA
    os.system('intersectBed -a ' + fname + ' -b ' + lncRNA + ' -wb > '+ project +'.tmp4')
    # #miRNA
    os.system('intersectBed -a ' + fname + ' -b ' + miRNA + ' -wb > '+ project +'.tmp5')
    # #piRNA
    os.system('intersectBed -a ' + fname + ' -b ' + piRNA + ' -wb > '+ project + '.tmp6')

    RnaEdits = readRnaEdits(project+'.bed')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp3', 0, 'circRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp4', 2, 'lncRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp5', 3, 'miRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp6', 4, 'piRNA')

    fout = open(project+'_ncRNA', 'w')
    Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        #print type(final[1])
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]))
            for key in final_pos_method[1]:
                fout.write('\t'+key+':'+final_pos_method[1][key])
            fout.write('\n')
    os.system('rm '+project+'.tmp*')

elif specie == 'rhesus':
    fname = project + '.bed'
    lncRNA = ncRNA_dir + 'lncRNA_noncode/NONCODEv5_rheMac3.lncAndGene.bed'
    miRNA = ncRNA_dir + 'miRNA_mirBase/macaca_mulatta.gff3'
    # #lncRNA
    os.system('intersectBed -a ' + fname + ' -b ' + lncRNA + ' -wb > '+ project +'.tmp4')
    # #miRNA
    os.system('intersectBed -a ' + fname + ' -b ' + miRNA + ' -wb > '+ project +'.tmp5')

    RnaEdits = readRnaEdits(project+'.bed')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp4', 4, 'lncRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp5', 3, 'miRNA')

    fout = open(project+'_ncRNA', 'w')
    Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        #print type(final[1])
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]))
            for key in final_pos_method[1]:
                fout.write('\t'+key+':'+final_pos_method[1][key])
            fout.write('\n')
    os.system('rm '+project+'.tmp*')

elif specie == 'nematode':
    os.system('python produce-bed.py '+project)
    fname = project + '.bed'
    # circRNA = ncRNA_dir + 'circRNA_circBase/cel_ce6_Memczak2013.txt'
    # lncRNA = ncRNA_dir + 'lncRNA_noncode/NONCODEv5_dm6.lncAndGene.bed'
    miRNA = ncRNA_dir + 'miRNA_mirBase/dya.gff3'
    # piRNA = ncRNA_dir + 'piRNA_piRBase/piR_dme_s.bed'
    # # circRNA
    # os.system('intersectBed -a ' + fname + ' -b ' + circRNA + ' -wb > '+ project +'.tmp3')
    # #lncRNA
    # os.system('intersectBed -a ' + fname + ' -b ' + lncRNA + ' -wb > '+ project +'.tmp4')
    # #miRNA
    os.system('intersectBed -a ' + fname + ' -b ' + miRNA + ' -wb > '+ project +'.tmp5')
    # #piRNA
    # os.system('intersectBed -a ' + fname + ' -b ' + piRNA + ' -wb > '+ project + '.tmp6')

    RnaEdits = readRnaEdits(project+'.bed')
    # RnaEdits = readncRNA(RnaEdits, project+'.tmp3', 0, 'circRNA')
    # RnaEdits = readncRNA(RnaEdits, project+'.tmp4', 4, 'lncRNA')
    RnaEdits = readncRNA(RnaEdits, project+'.tmp5', 3, 'miRNA')
    # RnaEdits = readncRNA(RnaEdits, project+'.tmp6', 4, 'piRNA')

    fout = open(project+'_ncRNA', 'w')
    Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
    for final in Sort_RnaEdits:
        final_chr = final[0]
        #print type(final[1])
        for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
            fout.write(final_chr + '\t' + str(final_pos_method[0]))
            for key in final_pos_method[1]:
                fout.write('\t'+key+':'+final_pos_method[1][key])
            fout.write('\n')
    #os.system('rm '+project+'.tmp*')
