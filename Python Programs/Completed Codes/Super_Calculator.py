#__function__
def Eq_Single(a,b,opr,x):
    if a=="x":
        a=x
    else:
        a= float(a)
    if b=="x":
        b=x
    else:
        b= float(b)
#    print("Processing:",a,opr,b)                                       # <- Debug
    if opr=="^":
        return round(a**b,10)
    elif opr=="/":
        return round(a/b,10)
    elif opr=="*":
        return round(a*b,10)
    elif opr=="+":
        return round(a+b,10)
    else:
        return round(a-b,10)

def Selector(fx,opr):
    ndx= None
    for i in range(len(fx)-1,-1,-1):
        if fx[i]==opr:
            ndx=i
            break
    n=1
    stin= 0
    enin= 0
    while True:         # Left of Operator
        try:
            if ndx-n>=0 and (fx[ndx-n].isdigit() or fx[ndx-n]=="." or fx[ndx-n]=="x"):
                n+=1
            elif ndx-n>=0 and fx[ndx-n]=="-" and (ndx-n)==0:
                stin= ndx-n
                n=1
                break
            elif ndx-n>=0 and fx[ndx-n]=="-" and (fx[ndx-n-1] in "^/*+-"):
                stin= ndx-n+1
                n=1
                break
            else:
                stin= ndx-n+1
                n=1
                break
        except IndexError:
            stin= ndx-n+1
            break
    while True:         # Right of Operator
        try:
            if fx[ndx+n].isdigit() or fx[ndx+n]=="." or fx[ndx+n]=="x":
                n+=1
            elif fx[ndx+1]=="-":
                n+=1
            else:
                enin= ndx+n-1
                break
        except IndexError:
            enin= ndx+n-1
            break
    return [ndx,stin,enin]

def Eq_Modify(fx,o,x):
#    print("__Running_Eq_Modify__")                      # <- Debug
    if "--" in "".join(fx):
        fx= list("".join(fx).replace("--","+"))
    elif "+-" in "".join(fx):
        fx= list("".join(fx).replace("+-","-"))
    l= Selector(fx,o)
    a= "".join(fx[l[1]:l[0]])
    b= "".join(fx[l[0]+1:l[2]+1])
#    print("a:",a)                                       # <- Debug
#    print("b:",b)                                       # <- Debug
#    print("Deleting: ","".join(fx[l[1]:l[2]+1]))        # <- Debug
    out= f"{Eq_Single(a,b,o,x):.10f}"
#    print("Inserting:",out)                             # <- Debug
    del fx[l[1]:l[2]+1]
    fx[l[1]:l[1]]= list(out)
#    print("Finally:","".join(fx))                       # <- Debug
    return fx

def Check_Num(s):
    try:
        t=float("".join(s))
#        print(t)                                        # <- Debug
        return True
    except ValueError:
        return False

def Eq_Mod_Seq(fx,x):
    lst= ["^","/","*","+","-"]
    for i in lst:
        while True:
            try:
                a= Eq_Modify(fx,i,x)
                fx= a
                if Check_Num(fx):
                    break
            except TypeError:
                break
            except ValueError:
                break
    return fx

def Exp_Solve(fx,x):
    return list(Eq_Mod_Seq(fx,x))

def Bracket_Reader(m,x):
    looping= True
    lst= list(m)
    while looping:
        stbrk= 0
        enbrk= 0
        eqn= ""
        for i in range(len(lst)):
            if lst[i]=="(":
                eqn= "("
                stbrk= i
            elif lst[i]==")":
                enbrk= i
                break
            else:
                eqn+=lst[i]
        if ("(" in lst or ")" in lst)==False:
            looping= False
        if looping:
            del lst[stbrk:enbrk+1]
            lst[stbrk:stbrk]= Exp_Solve(list(eqn.lstrip("(")),x)
    return lst

def Calculate(val,x=1,lno="Large Number Unable to Process"):
    mainstr= val.replace(" ","").replace("\n","").lower()
    try:
        OUT= "".join(Exp_Solve(Bracket_Reader(mainstr,x),x))
        return float(OUT)
#    except ValueError:
#        return lno
    except OverflowError:
        return lno

# Removes Hash to Do Normal Claculation, Keep Hash for Module Use
#__main__
#rn="y"
#while rn=="y":
#    valuein= input("Enter the Equation: ")
#    x= int(input("Enter the Value of x: "))
#    print("Answer: ",Calculate(valuein,x))
#    print()
#    rn= input("Run Again?(y/n): ").lower()
# "((x+5)^(x-1) + (x*2)^(x/2) - (x^3/(x-2))) * ((x+1)*(x-3)^2) / (x^4 + 1) + (x^(x/3) - (x+2)^(x-4))"
#print(Calculate("((x+5)^(x-1) + (x*2)^(x/2) - (x^3/(x-2))) * ((x+1)*(x-3)^2) / (x^4 + 1) + (x^(x/3) - (x+2)^(x-4))",990))
#print("Output:",Calculate("(x/200)^3 - (x/50)",-450))