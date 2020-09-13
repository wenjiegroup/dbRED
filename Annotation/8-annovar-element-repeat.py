import os
import sys
# recored repetitive elements
project = sys.argv[1]
os.system('python produce-bed.py '+project)
os.system('intersectBed -a '+project+'.bed -b reference/hg19.RepeatMasker.bed -wb > '+project+'-alu-nonalu.bed')
os.system('intersectBed -a '+project+'.bed -b reference/hg19.RepeatMasker.bed -v > '+project+'-nonrepeat.bed')

print 'finish intersectBed'

RnaEdits = {}

with open(project+'.bed') as f:
    for line in f.readlines():
        line = line.split('\t')
        chr = line[0]
        position = int(line[1])
        if chr not in RnaEdits:
            RnaEdits[chr] = {}
        RnaEdits[chr][position] = {}
print 'finish construct rnaedits dict'

with open(project+'-alu-nonalu.bed','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        Repeat = line[-1]
        Element = line[-3]+'/'+line[-2]
        if Repeat != 'Alu':
            RnaEdits[chr][position]['Repeat'] = 'Rep'
        else:
            RnaEdits[chr][position]['Repeat'] = Repeat
        RnaEdits[chr][position]['Element'] = Element

with open(project+'-nonrepeat.bed','r') as f:
    for line in f.readlines():
        line = line.strip().split('\t')
        chr = line[0]
        position = int(line[1])
        RnaEdits[chr][position]['Repeat'] = 'NonRep'
        RnaEdits[chr][position]['Element'] = '-/-'
print 'finish filling data'

#output the unique result
fout = open(project+'_repeat_element_result', 'w')
Sort_RnaEdits = sorted(RnaEdits.iteritems(), key = lambda a:a[0], reverse=False)
for final in Sort_RnaEdits:
    final_chr = final[0]
    #print type(final[1])
    for final_pos_method in sorted(final[1].iteritems(), key = lambda a:a[0], reverse=False):
        fout.write(final_chr + '\t' + str(final_pos_method[0]) + '\t' + final_pos_method[1]['Repeat']+ '\t' + final_pos_method[1]['Element'] + '\n')

os.system('rm '+project+'-alu-nonalu.bed')
os.system('rm '+project+'-nonrepeat.bed')
