#Made with Love by Utsav #COOOOOOL
import random as rn

# Code_Area:

def code_gen():
    rancodeerc_lst= []
    for i in range(3):
        rancodeerc_lst.append(rn.randint(10,40))
    for i in range(4):
        rancodeerc_lst.append(rn.randint(0,9))
    return rancodeerc_lst

def code_return():          # returns in format ["3260926587", [32, 60, 92, 6, 5, 8, 7]] '<-Format for var:code'
    cdlst= code_gen()
    codelst= []
    for i in cdlst:
        codelst.append(str(i))
    code= "".join(codelst)
    return [code,cdlst]

def code_break(x):          # returns in format [32, 60, 92, 6, 5, 8, 7] '<-Format for var:code'
    code=str(x)
    lst1= [int(code[0:2]),int(code[2:4]),int(code[4:6])]
    lst2= [int(code[-4]),int(code[-3]),int(code[-2]),int(code[-1]),]
    l= lst1+lst2
    return l

def duality(l):
    l1= [l[0],l[1],l[2]]
    l2= [l[3],l[4],l[5],l[6]]
    return [l1,l2]

def validate_code(c):
    retval= True
    c= str(c)
    if len(c)>10 or len(c)<10:
        retval= False
    if retval== True:
        l= [c[0:2],c[2:4],c[4:6]]
        for i in l:
           j= int(i)
           if j>40 or j<10:
               retval= False
    return retval


# Encrypt_Decrypt_Area

def en_de_crypt_lst(l,cd1,cd2):  # l= length of list or text
    l1= []
    l2= []
    while len(l1)<(l+1):
        for i in cd1:
            l1.append(i)
    while len(l2)<(l+1):
        for i in cd2:
            l2.append(i)
    return [l1,l2]

def chr_encrypt(w,x,y,z):           #here w=chr x= chr index, y= encrypt list1, z= +-encrypt list2
    poslist= [0,8,3,1,5]            #let x= 3 y= [11,22,33,11,22,33,11,22] z= [2,6,5,8,2,6,5,8,2,6,5,6,5,8]
    neglist= [7, 2, 4, 9, 6]
    newchr= "a"
    try:
        if z[x] in poslist:
            ordval= ord(w) +(y[x]*y[x+1] +(y[x]+y[x+1]))
            newchr= chr(ordval)
        elif z[x] in neglist:
            ordval= ord(w) +(y[x]*y[x+1] -(y[x]+y[x+1]))
            newchr= chr(ordval)
    except Exception:
        newchr= "�"
    return newchr

def chr_decrypt(w,x,y,z):
    poslist= [0,8,3,1,5]  
    neglist= [7, 2, 4, 9, 6]
    newchr= "a"
    try:
        if z[x] in poslist:
            ordval= ord(w) -(y[x]*y[x+1] +(y[x]+y[x+1]))
            newchr= chr(ordval)
        elif z[x] in neglist:
            ordval= ord(w) -(y[x]*y[x+1] -(y[x]+y[x+1]))
            newchr= chr(ordval)
    except Exception:
        newchr= "�"
    return newchr

def list_string(floc):
    with open(floc,"r",encoding="utf-8") as file:
        data= file.readlines()
    lenindex= [0]
    string= ""
    ct= 0
    for i in data:
        if "\n" in i:
            lenindex.append(len(i)-1+ct)
            ct+= len(i)-1
            string+= i[0:len(i)-1]
        else:
            lenindex.append(len(i)+ct)
            string+= i
    return [string,lenindex]

def string_list(strn,indxlst):
    lout= []
    for i in range(len(indxlst)-1):
        lout.append(strn[indxlst[i]:indxlst[i+1]]+"\n")
    lout[-1]= lout[-1][0:len(lout[-1])-1]
    return lout


# Menu_Area

def code_input(x=1):
    code= None
    if x==1:
        print("Would you like to Enter the Code Manually? (y/n),")
        c= input("  'n'-> generate's random code: ").lower()
    else:
        c= "y"
    inp= 1
    if c=="y":
        check= False
        while check== False:
            inp= int(input("Enter the 10-Digit Code: "))
            check= validate_code(inp)
            if check== False:
                print("InvalidCode: That is not the Type of Code For this Program")
            else:
                code= code_break(inp)
    else:
        lst= code_return()
        inp= int(lst[0])
        code= lst[1]
    if x==1:
        print("Your Code:",inp)
    else:
        print("Decryption Code Entered:",inp)
    return code

def backupfile(floc,c=0):
    lst= floc.split("\\")
    j= lst[-1]
    j= j.split(".")
    if c==1:
        j[0]+= "_Encrypted"
    else:
        j[0]+= "_Decrypted"
    j= ".".join(j)
    lst[-1]= j
    f= "\\".join(lst)
    return f


#__main__
runagain="y"
while runagain=="y":
    ch= 0
    while ch>4 or ch<1:
        print("Prefered langauge: English.")
        print("  1) Encrypt Text")
        print("  2) Encrypt File")
        print("  3) Decrypt Text")
        print("  4) Decrypt File")
        ch= int(input("Enter your choice: "))

    if ch==1:
        code= code_input()
        txt= input("Enter the text: ")
        encryptedtext= ""
        n= len(txt)
        for i in range(n):
            dualist= duality(code)
            erclst= en_de_crypt_lst(n,dualist[0],dualist[1])
            echar= chr_encrypt(txt[i],i,erclst[0],erclst[1])
            encryptedtext+= echar
        print(encryptedtext)

    elif ch==2:
        flocation= input("Enter the file location(Run in Admin mode for Restricted Area): ")
        try:
            lst= list_string(flocation)
        except Exception:
            print("FlieLocationErr: Directory",flocation,"Not Found")
            continue
        txt= lst[0]
        code= code_input()
        encryptedtext= ""
        n= len(txt)
        for i in range(n):
            dualist= duality(code)
            erclst= en_de_crypt_lst(n,dualist[0],dualist[1])
            echar= chr_encrypt(txt[i],i,erclst[0],erclst[1])
            encryptedtext+= echar
        fileinput= string_list(encryptedtext,lst[1])
        with open(backupfile(flocation,1),"w",encoding="utf-8") as file:
            file.writelines(fileinput)

    elif ch==3:
        code= code_input(1)
        txt= input("Enter the text: ")
        decryptedtext= ""
        n= len(txt)
        for i in range(n):
            dualist= duality(code)
            declst= en_de_crypt_lst(n,dualist[0],dualist[1])
            dchar= chr_decrypt(txt[i],i,declst[0],declst[1])
            decryptedtext+= dchar
        print(decryptedtext)
    
    elif ch==4:
        flocation= input("Enter the file location(Run in Admin mode for Restricted Area): ")
        try:
            lst= list_string(flocation)
        except Exception:
            print("FlieLocationErr: Directory",flocation,"Not Found")
            continue
        txt= lst[0]
        code= code_input(0)
        decryptedtext= ""
        n= len(txt)
        for i in range(n):
            dualist= duality(code)
            declst= en_de_crypt_lst(n,dualist[0],dualist[1])
            dchar= chr_decrypt(txt[i],i,declst[0],declst[1])
            decryptedtext+= dchar
        fileinput= string_list(decryptedtext,lst[1])
        with open(backupfile(flocation),"w",encoding="utf-8") as file:
            file.writelines(fileinput)
    
    runagain= input("Would you like to run again? (y/n): ").lower()

print("Enjoy your Day :)")