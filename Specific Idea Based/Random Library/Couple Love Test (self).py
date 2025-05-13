#importing modules
from libtype import AniType
from random import randint

#other info
width=35

#heading
print ("-"*width)
print (("Couple Love Test").center(width))
print ("-"*width)

while True:
    #inputs
    n1= input ("Enter Your Name \t : ")
    n2= input ("Enter Your Partner's name: ")
    print ()

    #processing
    res = randint (25,100)

    #printing output
    print (f"Your Love match is {res}%")
    hehe = "-"*(int((res-5)/4))
    
    # print (f"[{AniType(hehe)} {res}% {AniType(hehe)}]")

    print ("[",end="")
    AniType(hehe,0.03,0.2)
    print (f" {res}% ",end="")
    # print (res,"% ",end="")
    AniType(hehe,0.03,0.2)           
    print ("]")

    print (n1,"❤", n2)
    if res>80:
        print ("Ooo ma goo turu lobe ❤❤❤")

