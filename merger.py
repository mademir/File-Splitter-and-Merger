from os import listdir, remove, _exit
noMerge = True
filesDone = []
for i in listdir():
    if i[:8]=="mdemir1_":
        if i in filesDone: continue
        noMerge = False
        name = i
        filesDone.append(i)
        break
if noMerge: _exit(0)

while not noMerge:
    try:
        f1 = open(name, "rb")
        f2 = open(name[:6]+"2"+name[7:], "rb")
        res = open(f1.name[f1.name.index("_")+1:], "wb")
        res.write(f1.read()+f2.read())
        f1.close()
        f2.close()
        res.close()
    except:
        pass
    noMerge = True
    for i in listdir():
        if i[:8]=="mdemir1_":
            if i in filesDone: continue
            noMerge = False
            name = i
            filesDone.append(i)
            break
        
for z in listdir():
    if z[:6] == "mdemir": remove(z)
