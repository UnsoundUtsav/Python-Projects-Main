# Permutations and Combinations #

choice=0
while choice!=1 and choice!=2:
    print("Press :  ")
    print("  1 => for permutation.")
    print("  2 => for Combination.")
    print()
    choice= int(input("Enter your choice:"))
print()
print("Your Choice =>",choice)

if choice==1:
    print("Func.: Permutation")
    print()
else:
    print("Func.: Combination")
    print()
print("*[n is the total no. of digits]")
n= int(input("Enter the value of n: "))

nfact=1
rfact=1
nrfact=1

if choice==1:
    ncom= int(input("no. of common digits: "))
    lst=[]
    for i in range(ncom):
        lst.append(int(input("The number of times each occours: ")))
    pro=1
    for i in lst:
        for j in range(1,i+1):
            pro= pro*j
    
    for i in range(1,n+1):
        nfact= nfact*i
    
    val= (nfact/pro)
    print()
    print("Total no. of Arangements are: ",val)


elif choice==2:
    r= int(input("Enter how many Digits the Group should contain: "))
    for i in range(1,n+1):
        nfact= nfact*i
    for i in range(1,r+1):
        rfact= rfact*i
    for i in range(1,(n-r)+1):
        nrfact= nrfact*i

    val= nfact/(rfact*nrfact)
    print()
    print("Total no. of Combinations are: ",val)

else:
    sp=0
