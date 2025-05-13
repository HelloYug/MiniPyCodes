import pyautogui as pg
from pyperclip import copy
from webbrowser import open as siteopener
from time import sleep

def paste_emoji(emoji, times=1):
    copy(emoji)
    for _ in range(times):
        pg.hotkey("ctrl", "v")

def open_whatsapp(sleep_time=10):
    siteopener("https://web.whatsapp.com")
    sleep(sleep_time)

def open_group(group_name):
    pg.hotkey("ctrl", "alt", "/")
    sleep(1)
    if group_name == "Thakur ji":
        paste_emoji("\u0920\u093e\u0915\u0941\u0930 \u091c\u0940 \u0915\u093e \u0938\u093e\u0925")
    else:
        pg.typewrite(group_name)
    sleep(1)
    pg.press("enter")
    sleep(1)

def send_text(message):
    pg.typewrite(message)
    sleep(0.2)
    pg.press("enter")

def send_greeting(group, message, emoji):
    open_group(group)
    pg.typewrite(message)
    paste_emoji(emoji)
    sleep(0.2)
    pg.press("enter")

def close_tab():
    pg.hotkey("ctrl", "w")
