# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rnaedit.settings")
django.setup()
from RnaSearch.models import Cremanei_Rnaedit
path = '/home/zhaochenghui/GeneData/Rnaedit_result/'

def average(seq):
    return float(sum(seq)) / len(seq)

def main():
    f = open(path+'C.remanei_result','r')
    fin = open('human_rnaedit_num','r')
    n = int(fin.readlines()[0].strip())
    fin.close()

    for i in f.readlines():
        lis = i.split('\t')
        name = 'ce'+(6-len(str(n)))*'0'+str(n)
        Editlevel = float(lis[6])

        Cremanei_Rnaedit.objects.create(name=name, Chr = lis[0], position = int(lis[1]),\
        Strand = lis[2], Alt = lis[3], Ref = lis[4], \
        method = lis[5],  \
        Editlevel=Editlevel, \
        Sequence = lis[7], Cellline = lis[8])
        n += 1
        print n
    f.close()

    fout = open('human_rnaedit_num','w')
    fout.write(str(n)+'\n')
    fout.close()

if __name__ == '__main__':
    main()
