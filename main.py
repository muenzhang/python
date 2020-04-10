from listturtle import *
import turtle
from 疫情 import *
from IO import *
import time

list1=[]
list1=createlist(10)
list1=createpeople(list1,5)
list1=listrandom(list1)
writestr("","a.txt")

for i in range(5):
    list1=refresh2(list1,100,14,2)
    list1=refresh(list1)
    printlist(list1)
    write2dlist(list1,"a.txt")
    draw2dlist(list1,20,-200,200)
    sopeople(list1)
    time.sleep(1)
    turtle.reset()
draw2dlist(list1,20,-200,200)

writestr2("/","a.txt")
