import random as rn

s1= rn.randint(1,50)

c=0
cond= 2

if s1>=1 and s1<=10 :
    cond=0
elif s1>=11 and s1<=40 :
    cond=1

valdef= rn.randint(5,8)
valdef2= rn.randint(1,4)
ran1= rn.randint(1,s1+1)
ran50= rn.randint(s1,50)

print("")
print("--== Guess the Number b/w 1 and 50! ==--")
print("")
while c<5:
    s2= int(input("Enter the Guess: "))

    if s1==s2:
        c=6
        print(s1,"is the Right Number...Nice Guess!")

    else:
        c+=1
        print("Try Again...:(")
        print("")
        if c>2:
            if cond==0:
                print("The Number is bettween",ran1,"and",s1+(valdef2))
            elif cond==1:
                print("The Number is bettween",s1-(valdef2),"and",s1+(valdef2))
            else:
                print("The Number is bettween",s1-(valdef2),"and",ran50)
        elif c>0:
            if cond==0:
                print("The Number is bettween",ran1,"and",s1+(valdef))
            elif cond==1:
                print("The Number is bettween",s1-(valdef),"and",s1+(valdef))
            else:
                print("The Number is bettween",s1-(valdef),"and",ran50)

if c==5:
    print("The Number was",s1)
    print("YOU LOST :(")
else:
    print("YOU WIN :D")
