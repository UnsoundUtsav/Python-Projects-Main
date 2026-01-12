print("--==_BASE CONVERTER_==--")
print()
n= int(input("Enter a Number: "))
b= int(input("Enter the Base: "))

x=n
rem=0
quo=0
nolst= []

while n>=b-1:
    rem= n%b
    quo= n//b
    n=quo
    if rem>131:
        nolst.insert(0,chr(191+(rem-131))) 
    elif rem>9:
        nolst.insert(0,chr(96+(rem-9)).upper())
    else:
        nolst.insert(0,rem)
nolst.insert(0,quo)

print()
print("Output of ","(",x,")","↓",b," is:    ",sep="",end="")
for i in nolst:
    print(i,sep="",end="")


