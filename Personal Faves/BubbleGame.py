import turtle
import time
import math as m
import random
screen= turtle.Screen()
resx= 320
resy= 240

# __Playable Ball__
ball= turtle.Turtle("circle")
ball.penup()

# __Objects__
rad= 20
scl= rad/10

# Level Shape Type
l= int((resx*2)/(rad*2))
lb2= int(l/2)
b= int(((resy*2)/(rad*2))/3)
n= int(l*b)
print(n)
# __Creater__
objectlist= []
for i in range(n):
    objectlist.append(turtle.Turtle("circle"))
    objectlist[i].penup()
    objectlist[i].speed(0)
    objectlist[i].shapesize(stretch_wid=scl,stretch_len=scl)
    col= random.randint(1,4)
    if col==1:
        objectlist[i].color("red")
    elif col==2:
        objectlist[i].color("green")
    elif col==3:
        objectlist[i].color("blue")
    elif col==4:
        objectlist[i].color("yellow")
    print(i)


c=-1
for coll in range(b):
    for row in range(lb2):
        objectlist[c+row+1].goto(20+40*(row),20+40*(coll))
        print(c+row+1)
    c= row

c=32
for coll in range(b):
    for row in range(lb2):
        objectlist[c+row+1].goto(20+40*(row),20+40*(coll))
        print(c+row+1)
    c= 32+row



# __Functions__

#def Check_Intersection():

def Normal_Movement():
    global objectlist, factorlist, tick
    for i in range(len(objectlist)):
        curx= objectlist[i].xcor()
        cury= objectlist[i].ycor()
        x = curx + factorlist[i][3]*tick*m.cos(m.radians(factorlist[i][4]))
        y = cury + factorlist[i][3]*tick*m.sin(m.radians(factorlist[i][4]))
        objectlist[i].goto(x,y)


joe= input("yey")