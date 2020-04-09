def printtxt(name):
    f = open(name,"r",encoding="utf-8")
    print(f.read())
    f.close()

def writestr(str,name):
    with open(name,"w",encoding='utf-8') as f:
        f.write(str)

def writestr2(str,name):
    with open(name,"a",encoding='utf-8') as f:
        f.write(str)

def writelist(list,name):
    for j in range(len(list)-1):
        writestr2(str(list[j])+" ",name)
    writestr2(str(list[len(list)-1])+".",name)

def write2dlist(list,name):
    for i in range(len(list)-1):
        writelist(list[i],name)
        writestr2("\n",name)
    writelist("-",name)
    writestr2("\n",name)
