from listturtle import *
import turtle
from 疫情 import *


list1=[]
list1=createlist(10)
list1=createpeople(list1,10)
list1=listrandom(list1)


for i in range(5):
    list1=refresh2(list1,100,14,2)
    list1=refresh(list1)
    printlist(list1)
    draw2dlist(list1,20,-200,200)
    turtle.reset()
draw2dlist(list1,20,-200,200)
