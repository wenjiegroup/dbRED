# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rnaedit.settings")
django.setup()
from RnaSearch.models import Dvirilis_Rnaedit
path = '/home/zhaochenghui/GeneData/Rnaedit_result/'

def average(seq):
    return float(sum(seq)) / len(seq)

def main():
    f = open(path+'D.virilis_result','r')
    fin = open('human_rnaedit_num','r')
    n = int(fin.readlines()[0].strip())
    fin.close()

    for i in f.readlines():
        lis = i.split('\t')
        name = 'de'+(6-len(str(n)))*'0'+str(n)
        if lis[6] == 'synonymous SNV' or lis[6] == 'nonsynonymous SNV' or lis[6] == 'stoploss':
            Genename = lis[7].split(':')[0]
            Genedetail = ':'.join(lis[7].split(':')[1:])
            #print len(Genename)
            #print Genename, Genedetail
        else:
            if 'ENSMMUT' in lis[7]:
                Genename = lis[7].split('(')[0]
                Genedetail = lis[7].split('(')[1].split(')')[0]
            else:
                Genename = lis[7]
                Genedetail = None
        Editlevel = float(lis[9])

        Dvirilis_Rnaedit.objects.create(name=name, Chr = lis[0], position = int(lis[1]),\
        Strand = lis[2], Alt = lis[3], Ref = lis[4], \
        method = lis[5], \
        GeneRegion = lis[6], Genename = Genename, AAChange=lis[8], Editlevel=Editlevel, \
        Genedetail = Genedetail, \
        Sequence = lis[10], Cellline = lis[11])

        n += 1
        print n
    f.close()

    fout = open('human_rnaedit_num','w')
    fout.write(str(n)+'\n')
    fout.close()

if __name__ == '__main__':
    main()
