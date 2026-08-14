print("--==_Binomial_Expression_Generator_==--")
print()
while True:
    try:
        print("Formulae=  (x+y)^n or (x-y)^n")
        n= int(input("Enter the power: "))
        print("press: ")
        print("  1 => for Plus(+) sign")
        print("  2 => for Minus(-) sign")
        sign= int(input("Enter the Sign: "))
        break
    except ValueError:
        print("Invalid Input")
        pass

lstpasc= []
nfact=1
for i in range(1,n+1):
    nfact= nfact*i
    
for r in range(0,n+1):
    rfact=1
    for i in range(1,r+1):
        rfact= rfact*i
    nrfact=1
    for i in range(1,(n-r)+1):
        nrfact= nrfact*i

    din= rfact*nrfact
    pascal= nfact/din
    lstpasc.append(str(int(pascal)))

pow=0
lstxpow= []
lstypow=[]

for r in range(0,n+1):
    lstxpow.append(n-r)
    lstypow.append(r)

mainstring= ""

if sign==1:
    for i in range(n+1):
        if i==n:
            mainstring+= ("("+str(lstpasc[i])+"*x^"+str(lstxpow[i])+"*y^"+str(lstypow[i])+")")
        else:
            mainstring+= ("("+str(lstpasc[i])+"*x^"+str(lstxpow[i])+"*y^"+str(lstypow[i])+")"+" + ")
else:
    for i in range(n+1):
        if i==n:
            mainstring+= ("("+str(lstpasc[i])+"*x^"+str(lstxpow[i])+"*y^"+str(lstypow[i])+")")
        elif i%2==0:
            mainstring+= ("("+str(lstpasc[i])+"*x^"+str(lstxpow[i])+"*y^"+str(lstypow[i])+")"+" - ")

        else:
            mainstring+= ("("+str(lstpasc[i])+"*x^"+str(lstxpow[i])+"*y^"+str(lstypow[i])+")"+" + ")

print("Answer:",mainstring)

def Pasc_Calc(m):
    global n, sign
    try:
        x,y= int(input("Enter the value of X: ")), int(input("Enter the value of Y: "))
    except ValueError:
        x,y= 1,1
        pass
    lst= list(m)
    for j in range(len(lst)):
        if lst[j]=="y":
            lst[j]= str(y)
        elif lst[j]=="x":
            lst[j]= str(x)
    m= "".join(lst)
    print("Calculating:",m)
    if sign==1:
        return round((x+y)**n,2)
    else:
        return round((x-y)**n,2)

ch= input("Would you like to get Answer From the Equation?(y/n): ").lower()
if ch=="y":
    print("Answer: ",Pasc_Calc(mainstring))
else:
    pass