# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rnaedit.settings")
django.setup()
from RnaSearch.models import Rat_Rnaedit
path = '/home/zhaochenghui/GeneData/Rnaedit_result/'

def average(seq):
    return float(sum(seq)) / len(seq)

def main():
    f = open(path+'Rat_result','r')
    fin = open('human_rnaedit_num','r')
    n = int(fin.readlines()[0].strip())
    fin.close()

    for i in f.readlines():
        lis = i.split('\t')
        name = 'rn'+(6-len(str(n)))*'0'+str(n)
        if lis[10] == 'synonymous SNV' or lis[10] == 'nonsynonymous SNV' or lis[10] == 'stoploss':
            Genename = lis[11].split(':')[0]
            Genedetail = ':'.join(lis[11].split(':')[1:])
            #print len(Genename)
            #print Genename, Genedetail
        else:
            if 'ENSRNOT' in lis[11]:
                Genename = lis[11].split('(')[0]
                Genedetail = lis[11].split('(')[1].split(')')[0]
            else:
                Genename = lis[11]
                Genedetail = None
        Editlevel = float(lis[13])

        Rat_Rnaedit.objects.create(name=name, Chr = lis[0], position = int(lis[1]),\
        Strand = lis[2], Alt = lis[3], Ref = lis[4], dbSNP = lis[5], \
        method = lis[6], phastcons = float(lis[7]), Repeat = lis[8], Element=lis[9],\
        GeneRegion = lis[10], Genename = Genename, AAChange=lis[12], Editlevel=Editlevel, \
        Genedetail = Genedetail, lncRNA = lis[14], miRNA = lis[15], piRNA = lis[16], \
        circRNA = lis[17], Sequence = lis[18], Cellline = lis[19])
        n += 1
        print n
    f.close()

    fout = open('human_rnaedit_num','w')
    fout.write(str(n)+'\n')
    fout.close()

if __name__ == '__main__':
    main()
