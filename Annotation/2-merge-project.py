#coding:utf-8
#merge the A-to-I editing sites from multiple projects
import os
RnaEdits = {}
with open('encode_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        RnaEdits[chr][position] = {}
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'Encode:'+line[14]
        cellline = line[20]
        RnaEdits[chr][position]['others1'] = others1
        RnaEdits[chr][position]['others2'] = others2
        RnaEdits[chr][position]['others3'] = others3
        RnaEdits[chr][position]['method'] = method
        RnaEdits[chr][position]['editlevel'] = editlevel
        RnaEdits[chr][position]['cellline'] = cellline
        RnaEdits[chr][position]['project'] = 'Encode'
print 'encode complete...'

with open('roadmap_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'Roadmap:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'Roadmap'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';Roadmap'
print 'roadmap complete...'

with open('TCGA_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'CCLE:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'CCLE'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';CCLE'
print 'CCLE complete...'

with open('SEQC_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'SEQC:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'SEQC'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';SEQC'
print 'SEQC complete...'

with open('ABRF_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'ABRF:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'ABRF'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';ABRF'
print 'ABRF complete...'

with open('GEUV_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'GEUV:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'GEUV'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';GEUV'
print 'GEUV complete...'

with open('BrainDataSet_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'BrainDataSet:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'BrainDataSet'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';BrainDataSet'
print 'BrainDataSet complete...'

with open('HumanBodyMap_result','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        others1 = '\t'.join(line[2:7])
        others2 = '\t'.join(line[8:14])
        others3 = '\t'.join(line[15:20])
        method = line[7]
        editlevel = 'HumanBodyMap:'+line[14]
        cellline = line[20]
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        else:
            if position not in RnaEdits[chr]:
                RnaEdits[chr][position] = {}
                RnaEdits[chr][position]['others1'] = others1
                RnaEdits[chr][position]['others2'] = others2
                RnaEdits[chr][position]['others3'] = others3
                RnaEdits[chr][position]['method'] = method
                RnaEdits[chr][position]['editlevel'] = editlevel
                RnaEdits[chr][position]['cellline'] = cellline
                RnaEdits[chr][position]['project'] = 'HumanBodyMap'
            else:
                for i in method:
                    if i not in RnaEdits[chr][position]['method']:
                        RnaEdits[chr][position]['method'] += i
                RnaEdits[chr][position]['editlevel'] += ';'+editlevel
                RnaEdits[chr][position]['cellline'] += cellline
                RnaEdits[chr][position]['project'] += ';HumanBodyMap'
print 'HumanBodyMap complete...'

#output the unique result
fout = open('Human_final_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + final_pos_method[1]['others1']+ '\t' + final_pos_method[1]['method'] + '\t' + final_pos_method[1]['others2'] +'\t' + final_pos_method[1]['editlevel']+ '\t' + final_pos_method[1]['others3'] + '\t' + final_pos_method[1]['cellline'] + '\t' + final_pos_method[1]['project'] +'\n')
