#coding:utf-8
#using Annovar to annotate the gene information of sites
import os
import sys

project = sys.argv[1]

os.system('python preprocess_for_annovar.py '+project)
os.system('perl Transcript/1-MyCommand-for-Annovar-nematode.pl ' + project)
