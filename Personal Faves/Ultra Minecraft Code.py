import statistics as st
rerun= "y"

def portalspawn(pt):
    xi= pt[0]
    zi= pt[1]
    remx= xi%8
    remz= zi%8
    if  remx<=4:
        xi-= remx
    else:
        xi+= 8-remx
    if remz<=4:
        zi-= remz
    else:
        zi+= 8-remz

    return (xi,zi)



while rerun=="y":
    print("")
    print("Enter: ")
    print("(1)  For Optimal Coordinate from many points/Structures.")
    print("(2)  Optimal portal Spawn for Coordinate input")
    print("(3)  Convert Total Number to Stacks")
    
    choice= int(input("Enter your Choice: "))
    


    #Choices:
    if choice==1:
        n= int(input("Enter the no. of Points: "))
        print("Enter the input type:")
        print("(1)One-by-One    (2)Direct")
        nptype= int(input("Enter:"))
        lst= []

        if nptype==1:
            for i in range(n):
                print("")
                print("Point ",i+1,": ",sep="")
                x= int(input("Enter the x-axis: "))
                z= int(input("Enter the z-axis: "))
                lst.append((x,z))

            xtol= 0
            ztol= 0
            for i in lst:
                xtol+= i[0]
                ztol+= i[1]
            xmean= round(xtol/len(lst),0)
            zmean= round(ztol/len(lst),0)
            nearpt= (xmean,zmean)

            overcord= portalspawn(nearpt)
            nethercord= (overcord[0]/8,overcord[1]/8)

            print("Your Destination has Coordinates: ")
            print("Overworld Portal Spawn:"," "*4,"(",int(overcord[0]),",","~",",",int(overcord[1]),")",sep="")
            print("Required Nether Coordinates:"," "*4,"(",int(nethercord[0]),",","~",",",int(nethercord[1]),")",sep="")
        else:
            for i in range(n):
                print("")
                print("Point ",i+1,": ",sep="")
                loc= input("Enter in the form /tp x ~ z : ")
                loclst= loc.split(" ")
                x,z= int(loclst[1]),int(loclst[3])
                lst.append((x,z))

            xtol= 0
            ztol= 0
            for i in lst:
                xtol+= i[0]
                ztol+= i[1]
            xmean= round(xtol/len(lst),0)
            zmean= round(ztol/len(lst),0)
            nearpt= (xmean,zmean)

            overcord= portalspawn(nearpt)
            nethercord= (overcord[0]/8,overcord[1]/8)

            print("Your Destination has Coordinates: ")
            print("Overworld Portal Spawn:"," "*4,"(",int(overcord[0]),",","~",",",int(overcord[1]),")",sep="")
            print("Required Nether Coordinates:"," "*4,"(",int(nethercord[0]),",","~",",",int(nethercord[1]),")",sep="")


        rerun= input("Would you like to run the program again y/n: ").lower()



    elif choice==2:
        print("")
        print("Enter: ")
        print("1)  Overworld->Nether")
        print("2)  Nether->Overworld")

        ch= int(input("Enter the Choice: "))
        x= int(input("Enter the x-axis: "))
        z= int(input("Enter the z-axis: "))
        if ch==1:
            cord= portalspawn((x,z))
            print("Portal Location:  ","(",int(cord[0]/8),",","~",",",int(cord[1]/8),")",sep="")
        else:
            print("Portal Location:  ","(",x*8,",","~",",",z*8,")",sep="")

        rerun= input("Would you like to run the program again y/n: ").lower()



    elif choice==3:
        num= int(input("Enter the total no. of objects: "))
        stack= num//64
        sub= num%64

        print("Items: ",stack," Stack,",sub,sep="")

        rerun= input("Would you like to run the program again y/n: ").lower()


#Made With Love by Utsav Maity!!!



















