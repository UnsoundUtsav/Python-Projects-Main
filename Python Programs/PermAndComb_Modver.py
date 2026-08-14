from math import perm as P
from math import comb as C
from math import factorial as F

ch1=0
while ch1>2 or ch1<1:
    print("press: ")
    print("  1 => for Basic Permutation and Combination")
    print("  2 => for Advanced Permutation and Combination")
    ch1= int(input("Enter your choice: "))



if ch1==1:
    ch2=0
    while ch2>2 or ch2<1:
        print("  press: ")
        print("    1 => for Permutation(nPr)")
        print("    2 => for Combination(nCr)")
        ch2= int(input("Enter your choice: "))

    if ch2==1:
        n= int(input("Enter the Value of n: "))
        r= int(input("Enter the Value of r: "))
        print(n,"p",r,"= ",P(n,r),sep='')

    elif ch2==2:
        n= int(input("Enter the Value of n: "))
        r= int(input("Enter the Value of r: "))
        print(n,"c",r,"= ",C(n,r),sep='')



else:
    ch2=0
    print("  press: ")
    print("    1 => for Ways of Selection")
    print("    2 => for no. of ways Numbers could be Arranged")
    print("    3 => for Rank of a Word in Dictionary")
    print("    4 => ")
    print("    5 => ")
    print("    6 => ")
    ch2= int(input("Enter your choice: "))



    if ch2==1:
        objlst= []
        waylst= []
        n= int(input("Enter the no of objects: "))
        for i in range(n):
            objlst.append(int(input("No. of Events/Options is: ")))
            waylst.append(int(input("How many times/How many each time/How many: ")))

        c1=input("Does the ojects keep reducing with each cases(y/n): ")
        if c1=="y":
            n=1
            for i in range(len(objlst)):
                n*=P(objlst[i],waylst[i])
            print("Total no. of event(s) is/are: ",n)
    
        else:
            n=1
            for i in range(len(objlst)):
                n*=objlst[i]**waylst[i]
            print("Total no. of event(s) is/are: ",n)



    elif ch2==2:
        nlst= []
        s= str(input("Enter the no.: "))
        lst= list(s)
        for i in lst:
            nlst.append(int(i))

        condlst= []
        print("Conditions: ")
        condlst.append(int(input("Aranged in n digit places: ")))# index= 0
        condlst.append(input("Repetation allowed?(y/n): "))# index= 1
        condlst.append(int(input("> or < than any no.(*if not input 0): ")))# index= 2
        nw1gtlst= []
        x= str(condlst[2])
        nw1lst= list(x)
        for i in nw1lst:
            nw1gtlst.append(int(i))
        condlst.append(nw1gtlst)# index= 3



        if condlst[1]=="y":
            if condlst[2]==0:
                n= len(nlst)**condlst[0]
                print("Total no. of arrangements are:",n)
            else:
                print("Enter: (1)for Greater than; (2)for Less than")
                c= int(input("Enter the choice: "))
                if c==1:
                    bigno= []
                    x= str(condlst[2])
                    lust= list(x)
                    for i in lust:
                        bigno.append(int(i))
                    cntlst= []
                    for i in bigno:
                        cnt=0
                        for j in nlst:
                            if j>i:
                                cnt+=1
                                cntlst.append(cnt)
                    print(cntlst)
                    if 0 in cntlst:
                        cin= cntlst.index(0)
                    else:
                        cin= "skip"
                    val= 1
                    for i in range(0,cin):
                        val*= cntlst[i]
                    print(val)
                    if cin=="skip":
                        sp=0
                    else:
                        val*= len(cntlst)**(len(cntlst)-cin)
                    print("Total no. of arrangements are:",val)

                else:
                    indlst= []
                    for i in condlst[3]:
                        ind=0
                        for j in nlst:
                            if j<i:
                                ind+=1
                        indlst.append(ind)
                val=0
                for i in range(len(indlst)):
                    val+= indlst[i]*((len(indlst)-i)**(len(indlst)-i-1))

                    print("Total no. of arrangements are:",val)


        else:
            if condlst[2]==0:
                n=P(len(nlst),condlst[0])
                print("Total no. of arrangements are:",n)
            else:
                print("Enter: (1)for Greater than; (2)for Less than")
                c= int(input("Enter the choice: "))
                if c==1:
                    bigno= []
                    x= str(condlst[2])
                    lust= list(x)
                    for i in lust:
                        bigno.append(int(i))
                    cntlst= []
                    for i in bigno:
                        cnt=0
                        for j in nlst:
                            if j>i:
                                cnt+=1
                        cntlst.append(cnt)
                    print(cntlst)
                    if 0 in cntlst:
                        cin= cntlst.index(0)
                    else:
                        cin= "skip"
                    val= 1
                    for i in range(0,cin):
                        val*= cntlst[i]
                    if cin=="skip":
                        sp=0
                    else:
                        val*= F(len(cntlst)-cin)
                    print("Total no. of arrangements are:",val)
                else:
                    indlst= []
                    for i in condlst[3]:
                        ind=0
                        for j in nlst:
                            if j<i:
                                ind+=1
                        indlst.append(ind)
                val=0
                for i in range(len(indlst)):
                    val+= indlst[i]*F(len(indlst)-1)

                print("Total no. of arrangements are:",val)



    elif ch2==3:
        s= str(input("Enter the word: ")).upper()
        lst= list(s)
        arnlst= list(s)
        arnlst.sort()
        siu= list(arnlst)

        val= 0
        for i in range(len(lst)):
            common= 1
            e= None
            for k in arnlst:
                no= arnlst.count(k)
                if k==e:
                    sp= 0
                else:
                    common*= F(no)
                    e= k
            for j in arnlst:
                if lst[i]==j and lst[i]==arnlst[0]:
                    val+= F(len(lst)-i-1)/common
                    arnlst.remove(j)
                    break
                if lst[i]==j:
                    arnlst.remove(j)
                    break
                else:
                    val+= F(len(lst)-i-1)/common
        common= 1
        e= None
        for k in siu:
            no= siu.count(k)
            if k==e:
                sp= 0
            else:
                common*= F(no)
                e= k
        if common>1:
            print("Rank of",s,"is:",int(val-common+2))
        else:
            print("Rank of",s,"is:",int(val-2+(4-len(s))))



    elif ch2==4:
        print("Coming soon")





