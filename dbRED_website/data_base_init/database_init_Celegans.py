# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rnaedit.settings")
django.setup()
from RnaSearch.models import Celegans_Rnaedit
path = '/home/zhaochenghui/GeneData/Rnaedit_result/'

def average(seq):
    return float(sum(seq)) / len(seq)

def main():
    f = open(path+'C.elegans_result','r')
    fin = open('human_rnaedit_num','r')
    n = int(fin.readlines()[0].strip())
    fin.close()

    for i in f.readlines():
        lis = i.split('\t')
        name = 'ce'+(6-len(str(n)))*'0'+str(n)
        if lis[8] == 'synonymous SNV' or lis[8] == 'nonsynonymous SNV' or lis[8] == 'stoploss':
            Genename = lis[9].split(':')[0]
            Genedetail = ':'.join(lis[9].split(':')[1:])
            #print len(Genename)
            #print Genename, Genedetail
        else:
            if 'ENSMMUT' in lis[9]:
                Genename = lis[9].split('(')[0]
                Genedetail = lis[9].split('(')[1].split(')')[0]
            else:
                Genename = lis[9]
                Genedetail = None
        Editlevel = float(lis[11])

        Celegans_Rnaedit.objects.create(name=name, Chr = lis[0], position = int(lis[1]),\
        Strand = lis[2], Alt = lis[3], Ref = lis[4], \
        method = lis[5],  Repeat = lis[6], Element=lis[7],\
        GeneRegion = lis[8], Genename = Genename, AAChange=lis[10], Editlevel=Editlevel, \
        Genedetail = Genedetail, lncRNA = lis[12], miRNA = lis[13], piRNA = lis[14], \
        circRNA = lis[15], Sequence = lis[16], Cellline = lis[17])

        n += 1
        print n
    f.close()

    fout = open('human_rnaedit_num','w')
    fout.write(str(n)+'\n')
    fout.close()

if __name__ == '__main__':
    main()
