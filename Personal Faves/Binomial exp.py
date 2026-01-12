print("--==_Binomial_Expression_Generator_==--")
print()
print("Formulae=  (x+y)^n or (x-y)^n")
n= int(input("Enter the power: "))

print("press: ")
print("  1 => for Plus(+) sign")
print("  2 => for Minus(-) sign")
sign= int(input("Enter the Sign: "))

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

if sign==1:
    for i in range(n+1):
        if i==n:
            print("(",lstpasc[i],"*x^",lstxpow[i],"*y^",lstypow[i],")",sep="",end="")
        else:
            print("(",lstpasc[i],"*x^",lstxpow[i],"*y^",lstypow[i],")"," + ",sep="",end="")
else:
    for i in range(n+1):
        if i==n:
            print("(",lstpasc[i],"*x^",lstxpow[i],"*y^",lstypow[i],")",sep="",end="")
        elif i%2==0:
            print("(",lstpasc[i],"*x^",lstxpow[i],"*y^",lstypow[i],")"," - ",sep="",end="")

        else:
            print("(",lstpasc[i],"*x^",lstxpow[i],"*y^",lstypow[i],")"," + ",sep="",end="")




