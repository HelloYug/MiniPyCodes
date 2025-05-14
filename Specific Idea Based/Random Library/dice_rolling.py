# Dice Rolling
# Importing module
from random import randint

# Input
con = input("Do you want to roll the dice? (yes/no): ")

# Conditioning and printing output
while True:
    if con.lower() == "yes" or con.lower() == "y":
        print("Rolling the dice...")
        print("You got: ", randint(1, 6))
        print("*" * 35)
    else:
        print("Good bye, Thank you for using Python dice by Yug Agarwal")
        break
    
    con = input("Do you want to roll the dice again? (yes/no): ")
    if con.lower() in ["no", "n"]:
        print("Good bye, Thank you for using Python dice by Yug Agarwal")
        break
