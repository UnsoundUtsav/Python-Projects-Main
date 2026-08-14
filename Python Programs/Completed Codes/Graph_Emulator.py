import turtle, math, Super_Calculator

scr= turtle.Screen()
try:
    ax= int(input("Enter X-Resolution of Screen: "))
    ay= int(input("Enter Y-Resolution of Screen: "))
except ValueError:
    ax= 1980
    ay= 1080

print("Resoloution Set: ",ax,"x",ay,sep="")
ax= round(ax/2)
ay= round(ay/2)


# __function__
def Axis_Form(x=2*ax, y=2*ay):
    corder= turtle.Turtle()
    corder.hideturtle()
    corder.speed(0)
    corder.goto(x,0)
    corder.goto(-x,0)
    corder.goto(0,0)
    corder.goto(0,y)
    corder.goto(0,-y)

def trig(x,n):
    global prev
    try:
        if n==1:
            giv= math.tan(math.radians(x))
        elif n==2:
            giv= 1/math.cos(math.radians(x))
        elif n==3:
            giv= 1/math.sin(math.radians(x))
        elif n==4:
            giv= 1/math.tan(math.radians(x))
        if giv>0 and giv>=ay:
            return ay
        elif giv<0 and giv<=-ay:
            return -ay
        else:
            return giv
    except ValueError:
        if prev<0:
            return -ay
        else:
            return ay

def Eqn_make(x=0,stu=0,eqn=0):
    global ay
    while True and stu==0:
        print("<1> Select From Pre-Defined Functions <2> Make your own")
        ch= int(input("Enter your Choice: "))
        if ch==1:
            print("<1> Sin(x), "
            "<2> Cos(x), "
            "<3> Tan(x), "
            "<4> Sec(x), "
            "<5> Cosec(x), "
            "<6> Cot(x), "
            "<7> log(x), "
            "<8> e^x")
            ch= int(input("Enter your Choice: "))
            return ch
        else:
            return 0

    while True and stu==1:
        if eqn==1:
            return math.sin(math.radians(x))
        elif eqn==2:
            return math.cos(math.radians(x))
        elif eqn==3:
            return trig(x,1)
        elif eqn==4:
            return trig(x,2)
        elif eqn==5:
            return trig(x,3)
        elif eqn==6:
            return trig(x,4)
        elif eqn==7:
            try:
                return math.log(x,10)
            except ValueError:
                return 0
        elif eqn==8:
            try:
                giv= math.exp(x)
                if giv>ay:
                    return ay
                else:
                    return giv
            except ValueError:
                return ay

def Custom_Eqn(x):
    global val, ay
    return Super_Calculator.Calculate(val,x,ay)

def Curve_Gen(e=0, typ=0, x=ax,):
    curver= turtle.Turtle()
    curver.speed(0)
    curver.hideturtle()
    curver.goto(-x,0)
    curver.color("red")
    if typ==0:
        for i in range(-x,x+1):
            try:
                fx= round(Eqn_make(i,1,e),2)*100
                curver.goto(i,fx)
                if i%10==0:
                    print("(",i,",",fx,")")
            except Exception:
                pass
    else:
        for i in range(-x,x+1):
            fx= round(Custom_Eqn(i),2)
            curver.goto(i,fx)
            if i%10==0:
                print("(",i,",",fx,")")

# __main__
r= "y"
while r=="y":
    Axis_Form()
    eqn= Eqn_make()
    if eqn==0:
        print("Only basic calculations ie:- ^, /, *, +, - " \
        "and variable x and brackets()")
        val= input("Enter the Equation: ")
        Curve_Gen(eqn,1)
    else:
        Curve_Gen(eqn)
    r= input("Run Again?(y/n): ").lower()
    turtle.clearscreen()
