# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rnaedit.settings")
django.setup()
from RnaSearch.models import Human_Rnaedit
path = '/home/zhaochenghui/GeneData/Rnaedit_result/'

def average(seq):
    return float(sum(seq)) / len(seq)

def main():
    f = open(path+'Human_final_result','r')
    fin = open('human_rnaedit_num','r')
    n = int(fin.readlines()[0].strip())
    fin.close()

    for i in f.readlines():
        lis = i.split('\t')
        name = 're'+(8-len(str(n)))*'0'+str(n)
        if lis[11] == 'synonymous SNV' or lis[11] == 'nonsynonymous SNV' or lis[11] == 'stoploss':
            Genename = lis[12].split(':')[0]
            Genedetail = ':'.join(lis[12].split(':')[1:])
            #print len(Genename)
            #print Genename, Genedetail
        else:
            if 'ENST' in lis[12]:
                Genename = lis[12].split('(')[0]
                Genedetail = lis[12].split('(')[1].split(')')[0]
            else:
                Genename = lis[12]
                Genedetail = None
        Editlevels = lis[14].split(';')
        Editlevels = [float(i.split(':')[1]) for i in Editlevels]
        Editlevel = average(Editlevels)

        Human_Rnaedit.objects.create(name=name, Chr = lis[0], position = int(lis[1]),\
        Strand = lis[2], Alt = lis[3], Ref = lis[4], dbSNP = lis[5], database = lis[6],\
        method = lis[7], phastcons = float(lis[8]), Repeat = lis[9], Element=lis[10],\
        GeneRegion = lis[11], Genename = Genename, AAChange=lis[13], Editlevel=Editlevel, \
        Genedetail = Genedetail, lncRNA = lis[15], miRNA = lis[16], piRNA = lis[17], \
        circRNA = lis[18], Sequence = lis[19], Cellline = lis[20], Project = lis[21])
        n += 1
        print n
    f.close()

    fout = open('human_rnaedit_num','w')
    fout.write(str(n)+'\n')
    fout.close()

if __name__ == '__main__':
    main()
