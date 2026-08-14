import turtle, math, time, random

src= turtle.Screen()

vel= int(input("Enter Speed of Ball(pix/sec): "))
#vel= 10
tick= 0.01
rx= 320     # Resoloution X
ry= 240     # Resoloution Y
score= 0

pad= []
scrt = turtle.Turtle()
ball= turtle.Turtle("circle")
bste= [0,0,180,vel,False,0] # [x_cord, y_codr, +x_angle, mod_velocity(pix/tick), collision_state, collision_no]
pste= [0,vel*1.5]


# __functions__

def screen_setup():     # for __main__
    global rx, ry
    src.bgcolor("#3f81f2")
    turtle.setup(width= rx*2+100, height= ry*2+20, startx=100,starty=10)

    dot = turtle.Turtle()
    dot.hideturtle()
    dot.speed(0)
    dot.penup()
    dot.goto(-rx, ry)
    dot.pendown()
    dot.pensize(2)
    dot.fillcolor("#85b1ff")
    dot.begin_fill()
    dot.goto(rx, ry)
    dot.pencolor("#6298f5")
    dot.goto(rx, -ry)
    dot.pencolor("dark blue")
    dot.goto(-rx, -ry)
    dot.pencolor("#6298f5")
    dot.goto(-rx, ry)
    dot.pencolor("dark blue")
    dot.goto(rx, ry)
    dot.end_fill()

def game_setup():       # for __main__
    global pad, ball, scrt, rx, ry
    pad.append(turtle.Turtle("square"))
    pad.append(turtle.Turtle("square"))
    for i in pad:
        i.speed(0)
        i.color("black")
        i.shapesize(stretch_wid=3,stretch_len=0.5)
        i.penup()
    pad[0].setx(rx-5)
    pad[1].setx(-rx+5)

    scrt.hideturtle()
    scrt.penup()
    scrt.goto(0, ry-40)  # Top center
    scrt.color("blue")

    ball.penup()
    ball.speed(0)
    ball.shapesize(stretch_wid=0.5,stretch_len=0.5)
    ball.color("white")

def trig(inp,deg):
    if inp=="s":
        return math.sin(math.radians(deg))
    if inp=="c":
        return math.cos(math.radians(deg))
    if inp=="t":
        return math.tan(math.radians(deg))

def pad_mov_inp(x):
    global pste
    if x=="up" and pste[0]<ry-30:
        pad[0].sety(pste[0]+30)
        pad[1].sety(pste[0]+30)
        pste[0]+= 30
    elif x=="down" and pste[0]>-ry+30:
        pad[0].sety(pste[0]-30)
        pad[1].sety(pste[0]-30)
        pste[0]-= 30

def score_turt(x):
    global scrt, score
    if x==1:
        txt= "score: " +str(score)
        scrt.write(txt, align="center", font=("Arial", 20, "bold"))
    else:
        scrt.clear()

def degreset():         # for __main__
    global bste
    while bste[2]<0:
        bste[2]+= 360
    while bste[2]>=360:
        bste[2]-= 360

def Edge_Reflect():     # for __main__
    global bste, ry, vel
    apx= math.fabs(vel*trig("s",bste[2]))
    if bste[1]>=(ry-apx) or bste[1]<=(apx-ry):
        bste[2]= 360-bste[2]

def Ball_Move():        # for __main__
    global bste, ball, vel
    bste[0]+= vel*trig("c",bste[2])
    bste[1]+= vel*trig("s",bste[2])
    ball.goto(bste[0],bste[1])

def Ball_Touch_Pad():
    global bste, pste, rx, ry, vel, score
    apx= math.fabs(vel*trig("c",bste[2]))
    if (bste[1]<pste[0]+30 and bste[1]>pste[0]-30) and ((bste[0]<rx+5+apx and bste[0]>rx-5-apx) or (bste[0]<-rx+5+apx and bste[0]>-rx-5-apx)):
        bste[4]= True
        bste[5]+= 1
        if bste[5]==1:
            score+=1
            score_turt(0)
            score_turt(1)
        return True
    else:
        bste[4]= False
        return False

def Angle_Select():
    global pad, bste, pste  # 2 deg per pixel 
    if bste[0]>=0:
        if bste[1]>=pste[0]:
            bste[2]= 180-(2*(bste[1]-pste[0]))
        elif bste[1]<pste[0]:
            bste[2]= 180-(2*(bste[1]-pste[0]))
    elif bste[0]<0:
        if bste[1]>=pste[0]:
            bste[2]= (2*(bste[1]-pste[0]))
        elif bste[1]<pste[0]:
            bste[2]= 360-(2*(bste[1]-pste[0]))

def Pad_Reflect():      # for __main__
    if Ball_Touch_Pad() and bste[5]==1:
        Angle_Select()
    if (not Ball_Touch_Pad()) and bste[5]>1:
        bste[5]=0

def Ball_Miss():        # for __main__
    global ball, pad, bste, rx, vel
    apx= math.fabs(vel*trig("c",bste[2]))
    if bste[0]>=(rx+40+apx) or bste[0]<=(-rx-40-apx):
        bste[0], bste[1] = 0, 0
        ball.goto(0,0)
        bste[2]= random.randint(0,359)
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        print()

def Pad_Movement():     # for __main__
    src.listen()
    src.onkey(lambda: pad_mov_inp("up"),"Up")
    src.onkey(lambda: pad_mov_inp("down"),"Down")


#__main__

screen_setup()
game_setup()

for i in range(3,0,-1):
    print(i)
    time.sleep(1)

while True:
    degreset()
    Edge_Reflect()
    Pad_Reflect()
    Ball_Miss()
    Ball_Move()
    Pad_Movement()
    time.sleep(tick)

