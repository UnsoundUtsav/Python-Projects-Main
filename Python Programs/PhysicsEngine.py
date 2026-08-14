import turtle
import time
import math as m
import random
screen= turtle.Screen()

objectlist= []  
factorlist= []

n= int(input("Enter the no. of Elements: "))
print("<1> Enter Manually <2> Random Input")
ch= int(input("Enter your Choice: "))
resx= int(input("Enter Screen Edge Top Corner x: "))
resy= int(input("Enter Screen Edge Top Corner y: "))
print("Resolution: ",2*resx,"x",2*resy,sep="")

if ch==1:
    for i in range(n):
        objectlist.append(turtle.Turtle("circle"))
        objectlist[i].penup()
        objectlist[i].speed(0)
        objectlist[i].goto(int(input("Enter x:")),int(input("Enter y: ")))
        # Factors Input
        lstin= []
        lstin.append(i)                                 # index= 0 (index)
        lstin.append(int(input("Enter Mass: ")))        # index= 1 (Mass)
        lstin.append(int(input("Enter Radius:")))       # index= 2 (Radius)
        lstin.append(int(input("Enter Velocity:")))     # index= 3 (Velocity)
        lstin.append(int(input("Enter Angle:")))        # index= 4 (Angle)
        factorlist.append(lstin)
        scl= lstin[2]/10
        objectlist[i].shapesize(stretch_wid=scl,stretch_len=scl)

else:
    for i in range(n):
        objectlist.append(turtle.Turtle("circle"))
        objectlist[i].penup()
        objectlist[i].speed(0)
        objectlist[i].goto(random.randint(1-resx,resx-1),random.randint(1-resy,resy-1))
        # Factors Input
        lstin= []
        lstin.append(i)                          # index= 0 (index)
        lstin.append(random.randint(5,50))       # index= 1 (Mass)
        lstin.append(random.randint(32,96))      # index= 2 (Radius)
        lstin.append(random.randint(10,100))     # index= 3 (Velocity)
        lstin.append(random.randint(0,360))      # index= 4 (Angle)
        factorlist.append(lstin)
        scl= lstin[2]/10
        objectlist[i].shapesize(stretch_wid=scl,stretch_len=scl)

tick= 0.1

def Check_Intersection(i,j):
    global objectlist, factorlist
    o1= objectlist[i].position()
    o2= objectlist[j].position()
    r1= factorlist[i][2] 
    r2= factorlist[j][2]
    dy= o2[1]-o1[1]
    dx= o2[0]-o1[0]
    lcen= m.sqrt(dy*dy + dx*dx)
    sumr= r1+r2
    if lcen<=sumr:
        return (i,j)


def Inter_list():
    global objectlist
    intersectlst= []
    for i in range(len(objectlist)):
        for j in range(len(objectlist)):
            if i==j:
                continue
            else:
                k= Check_Intersection(i,j)
                if k!=None:
                    intersectlst.append(k)
    return intersectlst


def Collision_Effect(a,b):
    global objectlist, factorlist
    o1info= factorlist[a]
    o2info= factorlist[b]
    pos1= objectlist[a].position()      # (x1,y1)
    pos2= objectlist[b].position()      # (x2,y2)
    
    phi = m.degrees(m.atan2(pos2[1]-pos1[1], pos2[0]-pos1[0]))
    enot= o1info[4]
    theta= 180 + 2*phi - enot           # New Angle

    vnew= ((o1info[1]-o2info[1])*o1info[3]+2*o2info[1]*o2info[3])/(o1info[1]+o2info[1])     # New Velocity
    if vnew<0:
        vnew= -vnew
    elif vnew>0:
        theta= theta-180
    
    return [o1info[0],vnew,theta]


def All_Collision_Apply(lst):
    global factorlist
    alst= []
    for i in lst:
        alst.append(Collision_Effect(i[0],i[1]))
    for i in alst:
        factorlist[i[0]][3]= i[1]
        factorlist[i[0]][4]= i[2]


def Normal_Movement():
    global objectlist, factorlist, tick
    for i in range(len(objectlist)):
        curx= objectlist[i].xcor()
        cury= objectlist[i].ycor()
        x = curx + factorlist[i][3]*tick*m.cos(m.radians(factorlist[i][4]))
        y = cury + factorlist[i][3]*tick*m.sin(m.radians(factorlist[i][4]))
        objectlist[i].goto(x,y)

def Edge_Reflect(x=320,y=240):
    global objectlist, factorlist
    for i in range(len(objectlist)):
        l= objectlist[i].position()
        if l[0]>x or l[0]<-x:
            factorlist[i][4]= 180-factorlist[i][4]
        elif l[1]>y or l[1]<-y:
            factorlist[i][4]= -factorlist[i][4]

while 1==1:
    All_Collision_Apply(Inter_list())
    Edge_Reflect(resx,resy)
    Normal_Movement()
    time.sleep(tick)