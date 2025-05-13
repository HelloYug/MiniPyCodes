'''Romantic Greet GF'''
# ----------------------------------------------------------
'''Importing modules'''
from pyautogui import typewrite, press, hotkey
from webbrowser import open
from time import sleep
from random import choice

'''Website links'''
open("web.whatsapp.com")
# open("https://www.instagram.com/direct/inbox/")
sleep(15)

"""Message options"""
# message = '''Dear user,\nThis message is to inform you that your account is to be disabled for 0024 hours for using abusive language violating the terms of use.\nTeam IG,\nComunity Guidelines Management'''

Lovelist =["jaanu", "darling", "shona", "babu", "jaanemann", "sweetheart", "sugar cookie", "beautiful", "love", "cutiepie", "mera bacha", "mera jigar ka tukda", "rani", "babe", "baby", "dear future wife", "princess", "buttercup","Dream girl", "sunshine", "my gem", "angel", "doll", "chubby bubby", "baby girl", "teddy bear", "butterfly","my girl", "baby boo",  ]

"""Main program"""
count = 1
for i in Lovelist:
    typewrite(f"Good morning, {i.title()} <3")
    hotkey ("shift", "enter")

    typewrite(f"I love you! {(choice(Lovelist)).title()} <3")
    hotkey ("shift", "enter")

    typewrite(f"Have a nice day! <3")
    press("enter")

    print (f"message delivered {count} times")
    count += 1
