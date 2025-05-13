print ("Program Started")

# FGDM -->  Family Greetings Daily Messaging
from datetime import datetime, timedelta
timing = (datetime.now() + timedelta(0,7)).strftime("%H %M %S")
timing2 = "00 05 00"

# Impoting required modules
from pyautogui import hotkey, typewrite, press
from time import sleep, time
from random import choice
from pyperclip import copy
from string import emoticons
from webbrowser import open as siteopener # If want to open in system default browser
# from pywhatkit import whats # To open link in Chrome browser

path = "E:\\Yug's Storage\\Desktop\\Yug Study\\Programming\\CS Python\\Yug's Major Projects\\Whatsapp Greeting\\Log Files\\"

# Emoji printing
def copypaste (emoji, times = 1):
    copy (emoji)
    for i in range (times):
        hotkey ("ctrl", "V")

# Group Search
def Group (Name):
    hotkey ("ctrl", "alt", "/")

    if Name == "Thakur ji":
        copypaste ("ठाकुर जी का साथ")    
    else:
        typewrite (Name)

    sleep (0.6)
    press ("Enter")
    sleep (0.8)

# Open Browser
def OpenBrowser(Website_URL, SleepTime):
    # whats.open_web(Website_URL) #If want to open in Chrome browser
    siteopener (Website_URL) # If want to open in system default browser
    sleep (SleepTime)

def writing(data):
    for i in list(data):
        typewrite (i,0.01)
        if i == "\n":
            hotkey ("Shift", "Enter")
        if i in emoticons:
            copy (i)
            hotkey ("ctrl", "V")

def wishlogfiling(functioning, personname, chatorgroupname, starttime):
    alphatime = datetime.now().strftime("%H:%M:%S %d-%m-%Y (%a)")
    f = open (f"{path}WishWhatsAppLogFile.txt", "a")
    f.write (f"\nTime : {alphatime}")
    f.write (f"\n\tMessage Type : Wishing {functioning} to {personname}")
    f.write (f"\n\tChat Name    : {chatorgroupname}")
    f.write (f"\n\tTime taken   : {round(time() - starttime, 4)} Seconds")
    f.write ("\n" + "-"*60)
    f.close()

def greetlogfiling(GroupCount, starttime):
    alphatime = datetime.now().strftime("%H:%M:%S %d-%m-%Y (%a)")
    with open (f"{path}GreetWhatsAppLogFile.txt", "a") as f:
        f.write (f"\nTime : {alphatime}")
        f.write (f"\n\tGroups Wished : {GroupCount}")
        f.write (f"\n\tTime taken    : {round(time() - starttime, 4)} Seconds")
        f.write ("\n" + "-"*40)
        f.close()

# Anniversary wishing
def WishAnniversary (Groupname, Name_relationship_first, Name_relationship_second, Tareekh):
    if (datetime.now().strftime("%d %m")) == Tareekh:
        starttime = time()

        OpenBrowser ("web.whatsapp.com", 10)
        Group (Groupname)

        typewrite (f"Happy Anniversary {Name_relationship_first} and {Name_relationship_second} ")
        copypaste (choice (HeartList), 2)
        hotkey ("Shift", "Enter",)
        typewrite ("Wish you many many more years together!")
        copypaste ("🥳")
        copypaste (choice (HeartList))
        sleep (0.25)
        press ("Enter")
        sleep (1)
        hotkey ("ctrl", "W")

        wishlogfiling ("Anniversary", (f"{Name_relationship_first} & {Name_relationship_second}"), Groupname, starttime)

# Birthday Wishing
def WishBirthday (Groupname, Person_Name, Tareekh):
    if (datetime.now().strftime("%d %m")) == Tareekh:
        starttime = time()
        
        OpenBrowser ("web.whatsapp.com", 10)
        Group (Groupname)
        
        typewrite (f"Happy Birthday {Person_Name} ")
        copypaste ("🥳")
        copypaste (choice (HeartList))
        hotkey ("Shift", "Enter")
        typewrite ("Many many happy returns of the Day! ")
        copypaste ("🎉", 3)
        sleep (0.25)
        press ("Enter")
        sleep (1)
        hotkey ("ctrl", "W")

        wishlogfiling ("Birthday", Person_Name, Groupname, starttime)

# Initials
FamilyGroupList = ["Yug's", "Thakur ji", "Coz V R de family", "Baccha Party"]
FriendsGroupList = ["Tripod 🕺💃🕺", "Happy B. Birthday keeda 👾"]
Family_Message = ["Radhe radhe ", "Ram Ram "]
Friends_Message = ["Good morning!! ", "Mornaa!! ", "Morning!! "]
FlowersList = ["🌹", "🌼", "🌻", "🌸", "💐", "🌺", "🌷"]
HeartList = ["💕", "💖", "❤️", "💗", "❣️", "💞", "💓", "💝"]

# Main program
while True:
    if (datetime.now().strftime("%H %M %S")) == timing:
        betatime = time()
        OpenBrowser ("web.whatsapp.com", 18)
        count = 0
        for i in FamilyGroupList:
        
            Group (i)
            MessageSent = choice(Family_Message)
            typewrite (MessageSent)

            if MessageSent == "Radhe radhe ":
                copypaste ("🦚")
            else:
                copypaste ("🙏")

            copypaste (choice (FlowersList))
            sleep (0.2)
            press ("Enter")
            count += 1
                
        for i in FriendsGroupList:
            
            Group (i)
            MessageSent = choice (Friends_Message)
            typewrite (MessageSent)

            if MessageSent == "Mornaa!! ":
                copypaste (choice (HeartList))

            copypaste (choice (FlowersList))
            sleep (0.2)
            press ("Enter")
            count += 1
        
        sleep (1)
        hotkey ("Ctrl", "W")
        greetlogfiling (count, betatime)

    if (datetime.now().strftime("%H %M %S")) == timing2:
     
        # Wishing Anniversary to Mummy side Family
        WishAnniversary (FamilyGroupList[1], "Neelu Massi", "Parveen Masaji", "26 11" )
        WishAnniversary (FamilyGroupList[1], "Deepu Massi", "Alok Masaji", "17 02")
        WishAnniversary (FamilyGroupList[1], "Anu Massi", "Manoj Masaji", "07 02")
        WishAnniversary (FamilyGroupList[1], "Mamupagla", "Mami", "11 12")

        # Wishing Birthday to Mummy side family
        WishBirthday (FamilyGroupList[1], "Parveen Masaji", "23 02")
        WishBirthday (FamilyGroupList[1], "Neelu Massi", "26 06")
        WishBirthday (FamilyGroupList[1], "Vasu Bhaiya", "22 11")
        WishBirthday (FamilyGroupList[1], "Isha di", "15 04")
        WishBirthday (FamilyGroupList[1], "Alok Masaji", "06 06")
        WishBirthday (FamilyGroupList[1], "Deepu Massi", "16 02")
        WishBirthday (FamilyGroupList[1], "Anshul Bhaiya", "26 01")
        WishBirthday (FamilyGroupList[1], "Shaanvi", "23 01")
        WishBirthday (FamilyGroupList[1], "Manoj Masaji", "08 02")
        WishBirthday (FamilyGroupList[1], "Anu Massi", "03 01")
        WishBirthday (FamilyGroupList[1], "Deva", "15 05")
        WishBirthday (FamilyGroupList[1], "Mamupagla", "05 05")
        WishBirthday (FamilyGroupList[1], "Mami", "21 02")
        WishBirthday (FamilyGroupList[1], "Maanvi", "23 01")
        WishBirthday (FamilyGroupList[1], "Raghav", "08 12")

        # Wishing Anniversary to Papa side family
        WishAnniversary (FamilyGroupList[2], "Baba", "Maa", "15 06")
        WishAnniversary (FamilyGroupList[2], "Tauji", "Taiji", "08 07")
        WishAnniversary (FamilyGroupList[2], "Bua", "Fufaji", "11 12")
        WishAnniversary (FamilyGroupList[2], "Aastha didi", "Vishal Jiju", "16 11")

        # Wishing Birthday to Papa side Family
        WishBirthday (FamilyGroupList[2], "Baba", "05 01")
        WishBirthday (FamilyGroupList[2], "Maa", "08 12")
        WishBirthday (FamilyGroupList[2], "Tauji", "19 07")
        WishBirthday (FamilyGroupList[2], "Taiji", "19 01")
        WishBirthday (FamilyGroupList[2], "Ankur Bhai", "01 03")
        WishBirthday (FamilyGroupList[2], "Aakansha Di", "27 11")
        WishBirthday (FamilyGroupList[2], "Fufaji", "11 02")
        WishBirthday (FamilyGroupList[2], "Bua", "04 12")
        WishBirthday (FamilyGroupList[2], "Ishu Bhai", "05 10")
        WishBirthday (FamilyGroupList[2], "Aastha Di", "28 04")
        WishBirthday (FamilyGroupList[2], "Vishal Jiju", "22 06")

        # Wishing birthday to friends (Society)
        WishBirthday (FriendsGroupList[1], "Keeda", "14 11")
        WishBirthday (FriendsGroupList[1], "Rida", "28 04")
        WishBirthday (FriendsGroupList[1], "Avisha", "12 09")

        # Wishing birthday to friends (NOPS)
        WishBirthday (FriendsGroupList[0], "Arpii", "20 04")
        WishBirthday (FriendsGroupList[0], "Samaksh", "16 11")

    sleep (1)
