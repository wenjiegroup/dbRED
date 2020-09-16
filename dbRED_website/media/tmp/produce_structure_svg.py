import os
import sys

specie = sys.argv[1]
chr = sys.argv[2]
pos = sys.argv[3]
seq = sys.argv[4]
ref = sys.argv[5]

path = '/home/zhaochenghui/Rnaedit/static/image/'

alt_fout = open(specie+'_'+chr+'_'+pos+'_alt','w')
alt_fout.write('> '+specie+'_'+chr+'_'+pos+'_alt\n')
alt_fout.write(seq)
alt_fout.close()


ref_fout = open(specie+'_'+chr+'_'+pos+'_ref','w')
l = list(seq)
l[100] = ref
seq = ''.join(l)
ref_fout.write('> '+specie+'_'+chr+'_'+pos+'_ref\n')
ref_fout.write(seq)
ref_fout.close()

os.system('RNAfold --noPS -p < '+specie+'_'+chr+'_'+pos+'_ref > '+specie+'_'+chr+'_'+pos+'_ref_ss')
#os.system('gs -r100 -q -dNOPAUSE -dQUIET -dBATCH -dEPSCrop -dTextAlphaBits=4 -dGraphicsAlphaBits=2  -sDEVICE=png16m -sOutputFile='+path+specie+'_'+chr+'_'+pos+'_ref.png '+specie+'_'+chr+'_'+pos+'_ref_ss.ps')
os.system('java -cp VARNAv3-93.jar fr.orsay.lri.varna.applications.VARNAcmd -i '+specie+'_'+chr+'_'+pos+'_ref_ss -o '+path+specie+'_'+chr+'_'+pos+'_ref.svg -algorithm naview -annotations "AtoI:anchor=101,size=50,color=#ff000,type=B" -resulotion "2.0" -highlightRegion "101-101:outline=#ff0000" -baseInner "#334455"')
os.system('RNAfold --noPS -p < '+specie+'_'+chr+'_'+pos+'_alt > '+specie+'_'+chr+'_'+pos+'_alt_ss')
#os.system('gs -r100 -q -dNOPAUSE -dQUIET -dBATCH -dEPSCrop -dTextAlphaBits=4 -dGraphicsAlphaBits=2  -sDEVICE=png16m -sOutputFile='+path+specie+'_'+chr+'_'+pos+'_alt.png '+specie+'_'+chr+'_'+pos+'_alt_ss.ps')
os.system('java -cp VARNAv3-93.jar fr.orsay.lri.varna.applications.VARNAcmd -i '+specie+'_'+chr+'_'+pos+'_alt_ss -o '+path+specie+'_'+chr+'_'+pos+'_alt.svg -algorithm naview -annotations "AtoI:anchor=101,size=50,color=#ff000,type=B" -resulotion "2.0" -highlightRegion "101-101:outline=#ff0000" -baseInner "#334455"')
os.system('rm '+specie+'_'+chr+'_'+pos+'*')
