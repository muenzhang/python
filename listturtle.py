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
