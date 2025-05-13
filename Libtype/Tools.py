### Tools File
## Make your small tools to do short tasks here.
import libtype
print ("PROGRAM STARTED")

'''------------------------------------INDEX------------------------------------'''
 # --> Equation calculator
 # --> Code to remove all blank lines from a file
 # --> music playlist total length finder
 # --> onenote multi 100% viewer
 # --> find directories
 # --> mass stock changer
 # --> window screen finder
 # --> ms office recents remover
 # --> reach end of the website
 # --> 

 
'''----------------------------------------------------------------------------'''

'''----------------------------------------------------------------------------'''
'''Equation calculator'''
# n = eval (input("Enter the mathematical equation: "))
# print (f"Answer: {n}")

'''---------------------------------------------------------------------------'''
'''Code to remove all blank lines from a file'''
# FileAddress = ""

# string = ""
# with open (FileAddress, "r") as f:
#     for i in f:
#         if not i.isspace():
#             string += i

# with open (FileAddress, "w") as f:
#     for i in string:
#         f.write (i)

'''------------------------------------------------------------------------------'''
'''Music Playlist Total Length Finder'''
# path = "folder_path"
# from os import listdir, rename
# dir_list = listdir(path)

# print(f"Files and directories in '{path}' :")

# print(dir_list)

# def audio_duration(length):
# 	hours = length // 3600 # calculate in hours
# 	length %= 3600
# 	mins = length // 60 # calculate in minutes
# 	length %= 60
# 	seconds = length # calculate in seconds

# 	return int(hours), int(mins), int(seconds) # returns the duration

# def renameeree(ff):
# 	ff = ff.split("_")[1]
# 	dd = ""
# 	l = [4,6,8,10,12,14]
# 	count = 1
# 	for i in ff:
# 		dd += i
# 		if count in l:
# 			dd += " "
# 		count += 1

# 	return ("abc    " + dd)

# from mutagen.mp3 import MP3

# def show(timer):
# 	hours, mins, seconds = audio_duration(timer)
# 	if hours != 0:
# 		return('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
# 	else:
# 		return('Total Duration: {}:{}'.format(mins, seconds))

# timer = 0
# for i in (dir_list):
# 	if i.endswith(".mp3"):
# 		yug = f"{path}\\{i}"
# 		audio = MP3(yug)
# 		totalsec = audio.info.length
# 		print (yug, "\t", show(totalsec))
# 		timer += totalsec
# 		# nn = renameeree (yug)
# 		# rename(yug, f"{path2}\\{nn}")

# print ("\n" + show (timer) + "\n")

'''------------------------------------------------------------------------------'''
'''Onenote multi 100% viewer'''
# from pyautogui import press
# from time import sleep
# print ("started")
# sleep (4)
# for i in range (20):
#     press("alt")
#     sleep(0.06)
#     press ("down")
#     sleep(0.06)
#     press ("right", 5, 0.05)
#     sleep(0.06)
#     press ("enter")
#     sleep (4)
#     print (i+1)

'''------------------------------------------------------------------------------'''
''' Find Directeries'''
# from os import listdir, rename, walk, scandir, path
# from glob import glob

# path = "folder_path"

# l = listdir(path)
# print(1)
# for root,dirs,files in walk(path):
#     for f in files:
#          print(path.join(root, f))
#          print()

'''------------------------------------------------------------------------------'''
''' Mass Stock Changer '''
# from openpyxl import load_workbook
# file = "file_path"
# workbook = load_workbook (filename = file)
# wbsas = workbook["Sales & Stocks"]

# a = 2
# while wbsas[f"M{a}"].value != None:
#     ## Stock Call
#     # b = wbsas[f"M{a}"].value
#     # wbsas[f"I{a}"] = f"={b}"

#     ## All same (10)
#     # wbsas[f"I{a}"] = f"=10"
#     a += 1

# workbook.save(filename=file)

'''------------------------------------------------------------------------------'''
""" Window Screen Finder """
# from win32gui import GetWindowText, GetForegroundWindow
# from pyautogui import hotkey, press
# from time import sleep, time

# WindowName = "WhatsApp"
# CurrentScreen = GetWindowText(GetForegroundWindow())
# a = time()
# while True:
#     hotkey("super", "tab")
#     sleep (0.75)
#     press ("left")
#     sleep (0.25)
#     press ("enter")  

#     NewScreen = GetWindowText(GetForegroundWindow())

#     b = time()
#     print (NewScreen)
#     if NewScreen == WindowName:
#         break
#     elif NewScreen == CurrentScreen:
#         print ("No Window Found!")
#         break
#     elif (b - a) > 12:
#         print (b-a)
#         print ("System took More than 12 Seconds")
#         break

'''------------------------------------------------------------------------------'''
""" MS Office Recents Remover """
# from pyautogui import press, click
# from time import sleep
# sleep (3)
# for i in range(20):
#     click(button="right")
#     sleep (0.4)
#     press ("r")
#     sleep (0.6)
#     print (i)

'''------------------------------------------------------------------------------'''
""" Reach end of the website """
# from pyautogui import press
# from time import sleep
# sleep (3)
# for i in range (8):
#     press ("end")
#     sleep (2)

'''------------------------------------------------------------------------------'''
