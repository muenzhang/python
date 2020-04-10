import turtle
import time


def point(a):
    turtle.speed(0)
    turtle.pensize(3)
    turtle.pencolor(a)
    turtle.hideturtle()
    turtle.circle(1)

def drawpoint(x,y,a):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    point(a)

def drawlist(list,bc,y,x):
    turtle.pendown()
    for i in range(len(list)):
        if list[i]==1:
            drawpoint(x,y,"blue")
        elif list[i]==2:
            drawpoint(x,y,"red")
        elif list[i]>2:
            drawpoint(x,y,"orange")
        x+=bc

def draw2dlist(list,bc,x,y):
    for i in range(len(list)):
        drawlist(list[i],bc,y,x)
        y-=bc
        turtle.penup()
        turtle.goto(x,y)
    time.sleep(1)

def sopeople(list):
    a=0
    b=0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j]==2:
                a+=1
            if list[i][j]>2:
                b+=1
    turtle.goto(200,250)
    turtle.write("感染人数："+str(a),font=("宋体",15))
    turtle.goto(200,200)
    turtle.write("潜伏期人数："+str(b),font=("宋体",15))
