import random as rn

n= int(input("Enter the no. of Card play: "))
print("")
p1= []
p2= []
p3= []
p4= []
pall= [p1,p2,p3,p4]


#              #
# SHUFFLE PART #
#              #


# 1=red, 2=green, 3=blue, 4=yellow
for i in pall:
    prob= rn.randrange(0,41,5)
    spcard= int((prob/100)*n)
    nocard= n-spcard

    for j in range(spcard):
        got= rn.randint(1,4)

        #Colour Selection
        c= rn.randint(1,4)
        col= None
        if c==1:
            col= "Red"
        if c==2:
            col= "Green"
        if c==3:
            col= "Blue"
        if c==4:
            col= "Yellow"

        #Special Card Selection
        if got==1:
            i.append("+4")
        elif got==2:
            i.append("Colour Change")
        elif got==3:
            l=[]
            l.append(col)
            l.append("+2")
            i.append(l)
        else:
            l=[]
            l.append(col)
            l.append("Skip")
            i.append(l)

    for j in range(nocard):

        #Colour Selection
        c= rn.randint(1,4)
        col= None
        if c==1:
            col= "Red"
        if c==2:
            col= "Green"
        if c==3:
            col= "Blue"
        if c==4:
            col= "Yellow"

        #Number Card Selection
        l=[]
        l.append(col)
        l.append(rn.randint(1,9))
        i.append(l)

for x in pall:
    print(i)
print("You got: ")
print(pall[1])


#               #
# STARTING PART #
#               #


mycard= pall[0]
pall.pop(0)

CPL= [] #Main Card Play List !!!

#Start Card Colour Selection
c= rn.randint(1,4)
col= None
if c==1:
    col= "Red"
if c==2:
    col= "Green"
if c==3:
    col= "Blue"
if c==4:
    col= "Yellow"
#Start Card Number Selection
l=[]
l.append(col)
l.append(rn.randint(1,9))
CPL.append(l)

print("Start with:",l)


#               #
# GAMEPLAY PART #
#               #


skip= None
while len(pall[0])!=0 or len(pall[1])!=0 or len(pall[2])!=0 or len(mycard)!=0:

    #@            @#
    #@    BOTS    @#
    #@            @#

    #aplc= Applicable list
    for i in pall:
        ind1= pall.index(i)
        # SUPER IMPORTANT SKIP PART #
        if pall.index(i)==skip:
            continue
        #
        #WHOLE TTHING UNDER THIS INDENTATION GETS SKIPPPED !!!
        aplclst= []
        
        #aplc selection
        for j in i:
            if (CPL[-1][0]==j) or (CPL[-1][1]==j):
                aplclst.append(j)
            elif j=="Colour Change" or j=="+4":
                aplclst.append(j)

        #if nothing found (Add Card)
        if len(aplclst)==0:

            #Colour Selection
            c= rn.randint(1,4)
            col= None
            if c==1:
                col= "Red"
            if c==2:
                col= "Green"
            if c==3:
                col= "Blue"
            if c==4:
                col= "Yellow"

            probablity= rn.randint(1,100)
            got= rn.randint(1,4)

            if probablity<20:
                #Special Card Selection
                if got==1:
                    i.append("+4")
                elif got==2:
                    i.append("Colour Change")
                elif got==3:
                    l=[]
                    l.append(col)
                    l.append("+2")
                    i.append(l)
                else:
                    l=[]
                    l.append(col)
                    l.append("Skip")
                    i.append(l)

            else:
                #Number Card Selection
                l=[]
                l.append(col)
                l.append(rn.randint(1,9))
                i.append(l)

        # if card found 
        else:
            throw= aplclst[rn.randint(0,len(aplclst)-1)]
            CPL.append(throw)
            ind2= pall[ind1].index(throw)
            pall[ind1].pop(ind2)

        print("Player",ind1+2,"gives: ")
        print(CPL[-1])
        print(CPL)
        print("")
        for y in pall:
            print(y)
        #                    #
        #@ Effects For Bots @#
        #                    #

        if CPL[-1][0] in ["Red","Green","Blue","Yellow"]:

            j= pall[pall.index(i)+1]
            if CPL[-1][1] in [1,2,3,4,5,6,7,8,9]:    #j= pall[pall.index(i)+1] (J is the next player)
                None

            elif CPL[-1][1]=="Skip":
                givplay= pall.index(i)
                skip= giveplay+1

            elif CPL[-1][1]=="+2":
                for i in range(2):
                    #Colour Selection
                    c= rn.randint(1,4)
                    col= None
                    if c==1:
                        col= "Red"
                    if c==2:
                        col= "Green"
                    if c==3:
                        col= "Blue"
                    if c==4:
                        col= "Yellow"

                    probablity= rn.randint(1,100)

                    if probablity<20:
                        #Special Card Selection
                        if got==1:
                            j.append("+4")
                        elif got==2:
                            j.append("Colour Change")
                        elif got==3:
                            l=[]
                            l.append(col)
                            l.append("+2")
                            j.append(l)
                        else:
                            l=[]
                            l.append(col)
                            l.append("Skip")
                            j.append(l)

                    else:
                        #Number Card Selection
                        l=[]
                        l.append(col)
                        l.append(rn.randint(1,9))
                        j.append(l)

#        else:
#            if CPL[-1]=="Colour Change":










    #@            @#
    #@   PLAYER   @#
    #@            @#

    
    



























        
