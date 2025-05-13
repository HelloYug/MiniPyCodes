#Coin Toss (Get best out of N times)
#other info
width=25

#heading
print ("*"*width)
print (("TOSS GAME").center (width))
print ("*"*width)

#inputs
t1= input ("Enter Team 1 name: ")
t2= input ("Enter Team 2 name: ")

if t1=="":
    t1= "HEADS"

if t2=="":
    t2= "TAILS"

#importing module
from random import randint

if t1!="HEADS" and t2!="TAILS":
    print ("\n", t1, "VS", t2,"\n")
    
def game():
    ch=0
    ct=0
    n=1 #serial no.
    while True:
        c= randint (1,2)
        print (n,"\t",end="")
        n+=1
        
        if c == 1:
            print (t1,end="")
            ch+=1

        if c == 2:
            print (t2,end="")
            ct+=1

        a= input ("\t|")
        if a == "":
            continue
        else:
            print ("\n",ch, t1,"and", ct, t2)

            if ch>ct:
                print (t1,"is the winner")

            elif ch<ct:
                print (t2,"is the winner")
                    
            elif ch==ct:
                print ("The match is DRAW")
            break

#calling functions
while True:
    game()
    print("~"*28,"\n")
    ca= input ("Do you want to play again?")
    if ca=="n":
        print ("OK")
        break
    continue
