import random as rn
player1= str(input("Enter Your Name: "))

###################
##               ##
##  @FUNCTIONS@  ##
##               ##
###################


#                              #
# @RANDOM CARD MAKER FUNCTION@ #
#                              #
def randomcard(x,givenprob):

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

    probablity= rn.randint(x,100)
    got= rn.randint(1,4)
    l=[]

    if probablity<givenprob:
        #Special Card Selection
        if got==1:
            l.append("+4")
        elif got==2:
            l.append("Colour Change")
        elif got==3:
            l.append(col)
            l.append("+2")
        else:
            l.append(col)
            l.append("Skip")
    else:
        #Number Card Selection
        l.append(col)
        l.append(rn.randint(1,9))
    return l


#                         #
# @CARD EFFECTS FUNCTION@ #
#                         #
def cardeffects(player):

    if len(U_Set[-1])==2:
        # Basic Number Card Found:-
        if str(U_Set[-1][1]).isdigit():
            None

        # if Skip Card Found:-
        elif U_Set[-1][1]=="Skip":
            if player==mycard:
                skip.append(3)
                U_Set.append(U_Set[-2])
            else:
                skip.append(pall.index(player))
                U_Set.append(U_Set[-2])

        # if +2 Card Found:-
        elif U_Set[-1][1]=="+2":
            for t in range(2):
                player.append(randomcard(1,30))

    else:
        # if Colour Change Card Found:-
        if str(U_Set[-1][0])=="Colour Change":
            l= []
            #Colour Selection
            c= rn.randint(1,4)
            col= None
            if c==1:
                col= "Red"
            elif c==2:
                col= "Green"
            elif c==3:
                col= "Blue"
            elif c==4:
                col= "Yellow"
            if player==mycard:
                print("Bot 3 Changed the Colour to",col)
            elif player==pall[0]:
                print("You Changed the Colour to",col)
            elif player in pall:
                print("Bot",pall.index(player),"Changed the Colour to",col)

            l.append(col)
            l.append(10)
            U_Set.append(l)

        # if +4 Card Found:-
        elif str(U_Set[-1][0])=="+4":
            l= []
            #Colour Selection
            c= rn.randint(1,4)
            col= None
            if c==1:
                col= "Red"
            elif c==2:
                col= "Green"
            elif c==3:
                col= "Blue"
            elif c==4:
                col= "Yellow"
            if player==mycard:
                print("Bot 3 Changed the Colour to",col)
            elif player==pall[0]:
                print("You Changed the Colour to",col)
            elif player in pall:
                print("Bot",pall.index(player),"Changed the Colour to",col)

            l.append(col)
            l.append(10)
            U_Set.append(l)
            for t in range(4):
                player.append(randomcard(1,30))


#                                   #
# @APPLICABLE LIST MAKING FUNCTION@ #
#                                   #
def applicablelst(player):
    for j in player:                 # j is Card 

        if len(j)==1 and (len(U_Set[-1])==1 or len(U_Set[-1])==2):
            if j[0]=="Colour Change" or j[0]=="+4":
                aplclst.append(j)

        elif len(j)==2 and len(U_Set[-1])==2:
            if j[0]==U_Set[-1][0] or j[1]==U_Set[-1][1]:
                aplclst.append(j)


#                        #
# @BREAK CHECK FUNCTION@ #
#                        #
def breakcheck(player):

    # if Players Turn:-
    if player==mycard:
        if len(pall[-1])==0:
            brk= True

    # if Middle Bots Turn:-
    elif pall.index(i)>=1:
        if len(pall[pall.index(i)-1])==0:
            brk= True

    # if First Bots Turn:-
    elif pall.index(i)==0:
        if len(mycard)==0:
            brk= True



#               #
#   MAIN MENU   #
#               #

print("UNO!!!")
print("")

print("Rules: ")
print("1. just enter numbers .No need to enter card name (ie- just Enter 1 if you want to select the first card in the Deck)")
#print("2. ")
#print("")


n= int(input("Enter the no. of Card play: "))
gvprb= int(input("Enter the probablity for getting \
Super Cards(Select b/w 1-100)[Normal Gameplay: 30]: "))
print("")

me= []
b1= []
b2= []
b3= []
pall= [me,b1,b2,b3]

for i in pall:
    for j in range(n):
        i.append(randomcard(1,gvprb))

mycard= list(pall[0])
pall.pop(0)
print("You Got:",mycard)
print("")

#for i in pall:         #<= Experemental Data!!!
#    print(i)

U_Set= []
U_Set.append(randomcard(1,1))
print("The Game Starts With!:",U_Set[0])



#######################
##                   ##
##  @GAMEPLAY_PART@  ##
##                   ##
#######################

brk= None
skip= ["No Skip"]
while len(pall[0])!=0 and len(pall[1])!=0 and len(pall[2])!=0 and len(mycard)!=0:


    #              #
    #   Bot_Play   #
    #              #
    for i in pall:                  # i is Player
        breakcheck(i)
        cardeffects(i)
        #print(skip[-1])                 #<= Experemental Data!!!

        if brk==True:
            print("UNO!!!")
            break
        if skip[-1]==pall.index(i):
            continue

        else:
            skip.append("No Skip")
            # ind_Skip area:
            aplclst= []                 # aplclst= Applicable List 
            applicablelst(i)


            # if Card "NOT FOUND"
            if len(aplclst)==0:
                i.append(randomcard(gvprb//4,gvprb))
                print("")
                print("Bot",pall.index(i)+1,"picked a card from the deck")
                print("")

            # if Card "FOUND"
            else:
                cardind= rn.randint(0,len(aplclst)-1)
                card= aplclst[cardind]
                U_Set.append(card)
                i.remove(card)
                print("")
                print("Bot",pall.index(i)+1,"gave:",card,"    <---(Left with",len(i),"Card/s)")
                print("")


    #                    #
    #    Players_Turn    #
    #                    #
    breakcheck(mycard)
    cardeffects(mycard)
    for i in range(1):
        if brk==True:
            print("UNO!!!")
            break
        if skip==3:
            continue
        else:
            aplclst= []                 # aplclst= Applicable List 
            applicablelst(mycard)

            print("")
            print("Your cards:",mycard)
            print("")
            print("From Those you can give:",aplclst)
            print("")

            # if Card "NOT FOUND"
            if len(aplclst)==0:
                mycard.append(randomcard(gvprb//4,gvprb))
                print("You picked a card from the deck:",mycard[-1])
                print("")

            # Card Selection Menu For The Player(if Card "FOUND"):
            else:
                cardch=0
                while cardch>len(aplclst) or cardch<=0:
                    cardch= int(input("Enter the card number you want to give:"))

                cardpic= aplclst[cardch-1]
                U_Set.append(cardpic)
                mycard.remove(cardpic)
                print("You gave",cardpic,"    <---(Left with",len(mycard),"Card/s)")
                print("")

                if cardpic==['Colour Change'] or cardpic==['+4']:           # colourch= Colour Choice
                    colourch= 0
                    while colourch>4 or colourch<=0:
                        print("")
                        print("(1)Red   ,(2)Green   ,(3)Blue   ,(4)Yellow")
                        colourch= int(input("Enter the Colour: "))
                    if colourch==1:
                        colourch="Red"
                    elif colourch==2:
                        colourch="Green"
                    elif colourch==3:
                        colourch="Blue"
                    elif colourch==4:
                        colourch="Yellow"
                        
                    clst=[colourch,10]
                    U_Set.append(clst)



#################
##             ##
##  @WINNERS@  ##
##             ##
#################

pall.append(mycard)

winlst=[]

bt1= len(pall[0])
bt2= len(pall[1])
bt3= len(pall[2])
ply= len(pall[3])
all=[bt1,bt2,bt3,ply]

sall=sorted(all)
for i in sall:
    for j in pall:
        if len(j)==i:
            winlst.append(pall.index(j))

st1= ("Bot",winlst[0]+1)
nd2= ("Bot",winlst[1]+1)
rd3= ("Bot",winlst[2]+1)
th4= ("Bot",winlst[3]+1)
winlstact= [st1,nd2,rd3,th4]

#for i in winlstact:             #  <= Experemental Data 
#    print(i)

print("WINNER OF THIS MATCH!!!")
if winlstact[0]==('Bot', 4):
    print(player1,"!!!")
else:
    print(str(winlstact[0][0])+"_"+str(winlstact[0][1]),"!!!")
print("")

print("Leader Board:")
for i in winlstact:
    if i==('Bot', 4):
        print(player1)
    else:
        print(str(i[0])+"_"+str(i[1]))
