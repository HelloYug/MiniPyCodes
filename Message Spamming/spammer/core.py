# core.py
from pyautogui import hotkey, typewrite, press
from time import sleep
from pyperclip import copy
from string import emoticons
from webbrowser import open as siteopener
# from pywhatkit import whats  # Optional: open in Chrome

def copypaste(emoji: str, times: int = 1) -> None:
    """
    Copies an emoji and pastes it N times using Ctrl+V.
    """
    copy(emoji)
    for _ in range(times):
        hotkey("ctrl", "V")

def select_group(name: str) -> None:
    """
    Searches and opens the given WhatsApp group/chat.
    """
    hotkey("ctrl", "alt", "/")
    if name == "Thakur ji":
        copypaste("ठाकुर जी का साथ")
    else:
        typewrite(name)
    sleep(0.6)
    press("enter")
    sleep(0.8)

def open_browser(url: str, delay: float) -> None:
    """
    Opens the given website and waits.
    """
    # whats.open_web(url)  # Uncomment to use Chrome via pywhatkit
    siteopener(url)
    sleep(delay)

def send_message(data: str) -> None:
    """
    Sends the given message, handling emojis and line breaks.
    """
    for char in data:
        typewrite(char, 0.01)
        if char == "\n":
            hotkey("shift", "enter")
        if char in emoticons:
            copy(char)
            hotkey("ctrl", "V")
