'''Romantic Greet GF'''
# ----------------------------------------------------------

'''Importing modules'''
from pyautogui import press, hotkey
from time import sleep
from random import choice
from pyperclip import copy

"""Start Timer"""
print ("Starting in ....")
for i in range (4,0,-1):
    print (f"{i} Seconds")
    sleep (1)

Lovelist =["jaanu", "darling", "shona", "babu", "jaanemann", "sweetheart", "sugar cookie", "beautiful", "love", "cutiepie", "mera bacha", "mera jigar ka tukda", "rani", "babe", "baby", "dear future wife", "princess", "buttercup","Dream girl", "sunshine", "my gem", "angel", "doll", "chubby bubby", "baby girl", "teddy bear", "butterfly", "my girl", "baby boo",  ]
HeartList = ["💕", "💖", "❤️", "💗", "❣️", "💞", "💓", "💝"]
dugdugi = []

"""Main program"""
count = 1
for i in Lovelist:
    k = choice(Lovelist)
    dugdugi.append(k)

    word = choice(Lovelist)
    while word in dugdugi:
        word = choice(Lovelist)

    message = f"Good Morning, {k.title()} {choice(HeartList)}\nI love you! {word.title()} {choice(HeartList)}\nHave a nice day! {choice(HeartList)}"
    copy (message)
    sleep (0.04)
    hotkey ("ctrl", "V")

    press("enter")
    sleep (0.08)

    print (f"message delivered {count} times")
    count += 1
