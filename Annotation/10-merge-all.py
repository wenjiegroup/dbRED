#coding:utf-8

#outputfile format: chr pos strand alt ref dbsnp database method gerp repeat element GeneRegion Gene AAChange sequence Cellline ncRNA project

import os
import sys

def average(seq):
    return float(sum(seq)) / len(seq)

project = sys.argv[1]
specie = sys.argv[2]
path = '/public2/home/zhaoch/annovar/annotation_result/'+specie+'/'+project+'/'+project
#strand alt ref
strand_alt_ref = {}
f = open(path+'_strand_alt_ref_result','r')
for line in f.readlines():
    line = line.strip().split()
    chr = line[0]
    pos = int(line[1])
    strand = line[2]
    alt = line[3]
    ref = line[4]
    if chr not in strand_alt_ref:
        strand_alt_ref[chr] = {}
        strand_alt_ref[chr][pos] = strand+'\t'+alt+'\t'+ref
    else:
        strand_alt_ref[chr][pos] = strand+'\t'+alt+'\t'+ref
f.close()

#dbsnp
# dbsnp = {}
# f = open(path+'_dbsnp_result','r')
# for line in f.readlines():
#     line = line.split('\t')
#     chr = line[0]
#     pos = int(line[1])
#     if line[2] == '\n':
#         snp = '-'
#     else:
#         snp = line[2].strip()
#     if chr not in dbsnp:
#         dbsnp[chr] = {}
#         dbsnp[chr][pos] = snp
#     else:
#         dbsnp[chr][pos] = snp
# f.close()

#database
# database = {}
# f = open(path+'_database_result','r')
# for line in f.readlines():
#     line = line.split('\t')
#     chr = line[0]
#     pos = int(line[1])
#     if line[2] == '\n':
#         db = '-'
#     else:
#         db = line[2].strip()
#     if chr not in database:
#         database[chr] = {}
#         database[chr][pos] = db
#     else:
#         database[chr][pos] = db
# f.close()

#method
method = {}
f = open(project+'_final_result','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[0]
    pos = int(line[1])
    mt = line[2]
    if chr not in method:
        method[chr] = {}
        method[chr][pos] = mt
    else:
        method[chr][pos] = mt
f.close()

#gerp
# gerp = {}
# f = open(path+'_gerp.txt','r')
# for line in f.readlines():
#     line = line.strip().split('\t')
#     chr = line[0]
#     pos = int(line[1])
#     gp = line[2]
#     if chr not in gerp:
#         gerp[chr] = {}
#         gerp[chr][pos] = gp
#     else:
#         gerp[chr][pos] = gp
# f.close()

#Element Repeat
repeat_element = {}
f = open(path+'_repeat_element_result','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[0]
    pos = int(line[1])
    repeat = line[2]
    element = line[3]
    if chr not in repeat_element:
        repeat_element[chr] = {}
        repeat_element[chr][pos] = repeat+'\t'+element
    else:
        repeat_element[chr][pos] = repeat+'\t'+element
f.close()

#sequence
sequence = {}
f = open(path+'_sequence_result','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[0]
    pos = int(line[1])
    seq = line[4]
    if chr not in sequence:
        sequence[chr] = {}
        sequence[chr][pos] = seq
    else:
        sequence[chr][pos] = seq
f.close()

#Gene GeneRegion
Region_gene = {}
f = open(path+'.finalAnno.txt','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[0]
    pos = int(line[1])
    if len(line) < 5:
        gene_region = ''
        gene = ''
    else:
        gene_region = line[4]
        gene = line[5]
    if chr not in Region_gene:
        Region_gene[chr] = {}
        Region_gene[chr][pos] = gene_region+'\t'+gene
    else:
        Region_gene[chr][pos] = gene_region+'\t'+gene
f.close()

#aachange
AAChange = {}
f = open(path+'.exonic_variant_function','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[3]
    pos = int(line[4])
    aa = line[1]
    if chr not in AAChange:
        AAChange[chr] = {}
        AAChange[chr][pos] = aa
    else:
        AAChange[chr][pos] = aa
f.close()

#Cellline
Cellline = {}
f = open(path+'_cellline_sample_result','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[0]
    pos = int(line[1])
    cl = line[2]
    if chr not in Cellline:
        Cellline[chr] = {}
        Cellline[chr][pos] = cl
    else:
        Cellline[chr][pos] = cl
f.close()

#editinglevel
editinglevel = {}
f = open(path+'_editing_level','r')
for line in f.readlines():
    line = line.strip().split('\t')
    chr = line[0]
    pos = int(line[1])
    values = line[2].split(' ')
    value = [float(i) for i in values]
    editing = average(value)
    if chr not in editinglevel:
        editinglevel[chr] = {}
        editinglevel[chr][pos] = str(editing)
    else:
        editinglevel[chr][pos] = str(editing)
f.close()

#ncRNA
# lncRNA = {}
# circRNA = {}
# miRNA = {}
# piRNA = {}
# f = open(path+'_ncRNA','r')
# for line in f.readlines():
#     line = line.strip().split('\t')
#     chr = line[0]
#     pos = int(line[1])
#     if chr not in lncRNA:
#         lncRNA[chr] = {}
#         lncRNA[chr][pos] = ''
#     else:
#         lncRNA[chr][pos] = ''
#     if chr not in piRNA:
#         piRNA[chr] = {}
#         piRNA[chr][pos] = ''
#     else:
#         piRNA[chr][pos] = ''
#     if chr not in miRNA:
#         miRNA[chr] = {}
#         miRNA[chr][pos] = ''
#     else:
#         miRNA[chr][pos] = ''
#     if chr not in circRNA:
#         circRNA[chr] = {}
#         circRNA[chr][pos] = ''
#     else:
#         circRNA[chr][pos] = ''
#     for i in range(2, len(line)):
#         if 'lncRNA' in line[i]:
#             lr = line[i].split(':')[1]
#             lncRNA[chr][pos] = lr
#         elif 'piRNA' in line[i]:
#             pr = line[i].split(':')[1]
#             piRNA[chr][pos] = pr
#         elif 'miRNA' in line[i]:
#             mr = line[i].split(':')[1]
#             miRNA[chr][pos] = mr
#         elif 'circRNA' in line[i]:
#             cr = line[i].split(':')[1]
#             circRNA[chr][pos] = cr


fout = open(project+'_result', 'w')
Sort_RnaEdits = sorted(method.iteritems(), key = lambda a:a[0], reverse=False)
number = 0
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        if final_chr not in AAChange:
            AAChange[final_chr] = {}
            AAChange[final_chr][final_pos_method[0]] = 'unknown'
        else:
            if final_pos_method[0] not in AAChange[final_chr]:
                AAChange[final_chr][final_pos_method[0]] = 'unknown'
        # if final_pos_method[0] not in editinglevel[final_chr]:
        #     number += 1
        #     continue

        print final_chr, final_pos_method[0], method[final_chr][final_pos_method[0]]
        #Human Mouse
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + dbsnp[final_chr][final_pos_method[0]] + '\t' + database[final_chr][final_pos_method[0]] + '\t'\
        #  + method[final_chr][final_pos_method[0]] + '\t' + gerp[final_chr][final_pos_method[0]] + '\t'\
        #  + repeat_element[final_chr][final_pos_method[0]] + '\t' + Region_gene[final_chr][final_pos_method[0]] + '\t' \
        #  + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + lncRNA[final_chr][final_pos_method[0]] + '\t' + miRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + piRNA[final_chr][final_pos_method[0]] + '\t' + circRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        #D.melanogaster
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + database[final_chr][final_pos_method[0]] + '\t'\
        #  + method[final_chr][final_pos_method[0]] + '\t' \
        #  + repeat_element[final_chr][final_pos_method[0]] + '\t' + Region_gene[final_chr][final_pos_method[0]] + '\t' \
        #  + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + lncRNA[final_chr][final_pos_method[0]] + '\t' + miRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + piRNA[final_chr][final_pos_method[0]] + '\t' + circRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        # Rat
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + dbsnp[final_chr][final_pos_method[0]] + '\t' \
        #  + method[final_chr][final_pos_method[0]] + '\t' + gerp[final_chr][final_pos_method[0]] + '\t'\
        #  + repeat_element[final_chr][final_pos_method[0]] + '\t' + Region_gene[final_chr][final_pos_method[0]] + '\t' \
        #  + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + lncRNA[final_chr][final_pos_method[0]] + '\t' + miRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + piRNA[final_chr][final_pos_method[0]] + '\t' + circRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        #Chimpanzee Rhesus
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + dbsnp[final_chr][final_pos_method[0]] + '\t' \
        #  + method[final_chr][final_pos_method[0]] + '\t' \
        #  + repeat_element[final_chr][final_pos_method[0]] + '\t' + Region_gene[final_chr][final_pos_method[0]] + '\t' \
        #  + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + lncRNA[final_chr][final_pos_method[0]] + '\t' + miRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + piRNA[final_chr][final_pos_method[0]] + '\t' + circRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        #C.elegans
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + method[final_chr][final_pos_method[0]] + '\t'\
        #  + repeat_element[final_chr][final_pos_method[0]] + '\t' + Region_gene[final_chr][final_pos_method[0]] + '\t' \
        #  + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + lncRNA[final_chr][final_pos_method[0]] + '\t' + miRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + piRNA[final_chr][final_pos_method[0]] + '\t' + circRNA[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        #C.briggsae D.ananassae D.simulans D.yakuba D.pseudoobscura
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
         + method[final_chr][final_pos_method[0]] + '\t'\
         + repeat_element[final_chr][final_pos_method[0]] + '\t' + Region_gene[final_chr][final_pos_method[0]] + '\t' \
         + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
         + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        #D.mojavensis D.virilis
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + method[final_chr][final_pos_method[0]] + '\t'\
        #  + Region_gene[final_chr][final_pos_method[0]] + '\t' \
        #  + AAChange[final_chr][final_pos_method[0]] + '\t' + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')

        #C.brenneri C.japonica C.remanei
        # fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + strand_alt_ref[final_chr][final_pos_method[0]] +'\t'\
        #  + method[final_chr][final_pos_method[0]] + '\t'\
        #  + editinglevel[final_chr][final_pos_method[0]] +'\t'\
        #  + sequence[final_chr][final_pos_method[0]]  + '\t' + Cellline[final_chr][final_pos_method[0]] +'\n')
