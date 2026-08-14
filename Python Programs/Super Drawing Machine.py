print("_-==SUPER DRAWING MACHINE==-_")
print("*Made with Love by Utsav Maity")
print("")
nr= int(input("Enter the Number of Rows: "))
nc= int(input("Enter the Number of Collumns: "))
n= int(input("Enter the Size of triangle: "))
print("")
print("")
trlst_tot= []
inplst_tot= []

print("Enter: ")
print("  1 => Step by Step Input")
print("  2 => Direct Input")
choice= int(input("Enter the Input Method: "))


if choice==1:
    for i in range(nc):
        print(" ")
        print("    Collumn-",i+1,sep="")
        trlst= []
        inplst= []
        for j in range(2*nr):
            print("")
            print("press: ")
            print("  (1) => For Straight Triangle")
            print("  (2) => For Inverted Triangle")
            print("")
            print("   #TRIANGLE-",j+1,sep="")
            trlst.append(input("Enter the triangle Type_(1/2): "))
            inplst.append(input("Enter the Paint_(*Use Space-' '  for empty input): "))
        trlst_tot.append(trlst)
        inplst_tot.append(inplst)

elif choice==2:
    for i in range(nc):
        print("Collum:-",i+1)
        trlst_tot.append(list(eval(input("Enter the Triangle_code: "))))#eg.- [['1','1','2','2'],['2','2','1','1']]
        inplst_tot.append(list(eval(input("Enter the Colour_code: "))))#eg.- [[' ','#',' ',' '],[' ','#',' ',' ']]
        print("")


print(trlst_tot)
print(inplst_tot)
print("")



for x in range(1,nc+1):
    for i in range(n):
        for y in range(1,2*nr+1):
            if trlst_tot[x-1][y-1]== "2":
                for j in range(n-i):
                    print(inplst_tot[x-1][y-1],end="")
            elif trlst_tot[x-1][y-1]== "1":
                if inplst_tot[x-1][y-1]== " " and x%2==0:
                    for j in range(i):
                        print(inplst_tot[x-1][y-1],end="")
                else:
                    for j in range(i):
                        print(inplst_tot[x-1][y-1],end="")
        print("")
