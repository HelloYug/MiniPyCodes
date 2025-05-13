#Dice rolling
#importing module
from random import randint

#input
con= input ("Do you want to roll the dice?: ")

#conditioning and printing output
while True:
    print ("Rolling the dice...")
    print ("You got: ",randint(1,6))
    print ("*"*35)

    con= input ("Do you want to roll the dice again?: ")
    if con=="no" or con=="n":
        print ("Good bye, Thank you for using Python dice by Yug Agarwal")
        break   
    continue
