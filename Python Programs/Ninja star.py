n= int(input("Size: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    print("")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(n-i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(n-i):
        print(" ",end="")
    print("")
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    print("")

