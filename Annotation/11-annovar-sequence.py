#coding: utf-8
#extract sequence surrounding A-to-I editing sites
import os
import sys

project = sys.argv[1]

input = project+"_strand_alt_ref_result"
output = project+"_sequence_result"

os.system("perl ./Transcript/0-Feature_Sequence.pl "+input+" "+output)
