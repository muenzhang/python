import random


def createlist(c):
    a=[]
    b=[]
    for i in range(c):
        b=[]
        for j in range(c):
            b.append(0)
        a.append(b)
    return a

def printlist(a):
    for i in range(len(a)):
        print(a[i])
    print()

def createpeople(list,people):
    for i in range(len(list)-1):
        for j in range(people):
            list[i][j]=1
    list[0][0]=2
    return list

def listrandom(list):
    for i in range(len(list)):
        for i in range(len(list[i])):
            random.shuffle(list[i])
        random.shuffle(list)
    return list

def goto(list,x,y,a):
    if list[y][x]!=0:
        if a==1:
            if y-1>=0 and list[y-1][x]!=1 and list[y-1][x]!=2:
                list[y-1][x]=list[y][x]
                list[y][x]=0
        if a==2:
            if y+1<len(list) and list[y+1][x]!=1 and list[y+1][x]!=2:
                list[y+1][x]=list[y][x]
                list[y][x]=0    
        if a==3:
            if x-1>=0 and list[y][x-1]!=1 and list[y][x-1]!=2:
                list[y][x-1]=list[y][x]
                list[y][x]=0
        if a==4:
            if x+1<len(list[y]) and list[y][x+1]!=1 and list[y][x+1]!=2:
                list[y][x+1]=list[y][x]
                list[y][x]=0

    return list

def refresh(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j]!=0:
                list=goto(list,j,i,random.randint(1,4))
    return list

def disease(list,a,x,y):
    if y+1<len(list) and list[y+1][x]==2:
        b=random.randint(1,100)
        if b<=a:
            list[y][x]=2
            
    if y-1>-1 and list[y-1][x]==2:
        b=random.randint(1,100)
        if b<=a:
            list[y][x]=2
            
    if y+1<len(list) and x+1<len(list[0]) and list[y+1][x+1]==2:
        b=random.randint(1,100)
        if b<=a:
            list[y][x]=2
            
    if y+1<len(list) and x-1>-1 and list[y+1][x-1]==2:
        b=random.randint(1,100)
        if b<=a:
            list[y][x]=2

    if y>-1 and x+1<len(list[0]) and list[y-1][x+1]==2:
        b=random.randint(1,100)
        if b<=a:
            list[y][x]=2

    if y-1>-1 and x-1>-1 and list[y-1][x-1]==2:
        b=random.randint(1,100)
        if b<=a:
            list[y][x]=2
    return list

def refresh2(list,s):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j]==1:
                list=disease(list,s,i,j)
    return list



