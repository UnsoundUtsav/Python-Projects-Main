from math import perm as P
from math import comb as C
from math import factorial as F

while 1==1:
    while 1==1:
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



