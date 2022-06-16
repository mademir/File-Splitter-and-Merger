import sys
from os.path import basename
if len(sys.argv)==2: f = open(basename(sys.argv[1]),"rb")
else: f = open(str(input("Enter file name to split:\t")), "rb")
bfa = f.read()
fh = open("mdemir1_"+f.name, "wb")
sh = open("mdemir2_"+f.name, "wb")
fh.write(bfa[:len(bfa)//2])
sh.write(bfa[len(bfa)//2:])
fh.close()
sh.close()
f.close()
