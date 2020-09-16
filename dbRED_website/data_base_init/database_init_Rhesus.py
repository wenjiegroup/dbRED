# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rnaedit.settings")
django.setup()
from RnaSearch.models import Rhesus_Rnaedit
path = '/home/zhaochenghui/GeneData/Rnaedit_result/'

def average(seq):
    return float(sum(seq)) / len(seq)

def main():
    f = open(path+'Rhesus_result','r')
    fin = open('human_rnaedit_num','r')
    n = int(fin.readlines()[0].strip())
    fin.close()

    for i in f.readlines():
        lis = i.split('\t')
        name = 'rh'+(6-len(str(n)))*'0'+str(n)
        if lis[9] == 'synonymous SNV' or lis[9] == 'nonsynonymous SNV' or lis[9] == 'stoploss':
            Genename = lis[10].split(':')[0]
            Genedetail = ':'.join(lis[10].split(':')[1:])
            #print len(Genename)
            #print Genename, Genedetail
        else:
            if 'ENSMMUT' in lis[10]:
                Genename = lis[10].split('(')[0]
                Genedetail = lis[10].split('(')[1].split(')')[0]
            else:
                Genename = lis[10]
                Genedetail = None
        Editlevel = float(lis[12])

        Rhesus_Rnaedit.objects.create(name=name, Chr = lis[0], position = int(lis[1]),\
        Strand = lis[2], Alt = lis[3], Ref = lis[4], dbSNP = lis[5], \
        method = lis[6],  Repeat = lis[7], Element=lis[8],\
        GeneRegion = lis[9], Genename = Genename, AAChange=lis[11], Editlevel=Editlevel, \
        Genedetail = Genedetail, lncRNA = lis[13], miRNA = lis[14], piRNA = lis[15], \
        circRNA = lis[16], Sequence = lis[17], Cellline = lis[18])
        n += 1
        print n
    f.close()

    fout = open('human_rnaedit_num','w')
    fout.write(str(n)+'\n')
    fout.close()

if __name__ == '__main__':
    main()
