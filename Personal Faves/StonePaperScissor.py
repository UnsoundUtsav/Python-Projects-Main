from random import randint as rn

c="y"
while c=="y":
    out= rn(1,3)
    print("StonePaperScissor CUT!")
    if out==1:
        print("Stone!")
    elif out==2:
        print("Paper!")
    elif out==3:
        print("Scissor!")
    else:
        print("wtf")
    c= input("Again? (y/n): ")
    
