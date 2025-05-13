from random import choice

FAMILY_GROUPS = ["Yug's", "Thakur ji", "Coz V R de family", "Baccha Party"]
FRIENDS_GROUPS = ["Tripod 🕺💃🕺", "Happy B. Birthday keeda 💾"]

FAMILY_MESSAGES = ["Radhe radhe ", "Ram Ram "]
FRIENDS_MESSAGES = ["Good morning!! ", "Mornaa!! ", "Morning!! "]
FLOWERS = ["🌹", "🌼", "🌻", "🌸", "💐", "🌺", "🌷"]
HEARTS = ["💕", "💖", "❤️", "💗", "❣️", "💞", "💓", "💝"]

BIRTHDAYS = {
    "23 02": [("Parveen Masaji", FAMILY_GROUPS[1])],
    "15 04": [("Isha di", FAMILY_GROUPS[1])],
    "05 01": [("Baba", FAMILY_GROUPS[2])],
    "28 04": [("Aastha Di", FAMILY_GROUPS[2]), ("Rida", FRIENDS_GROUPS[1])],
    "20 04": [("Arpii", FRIENDS_GROUPS[0])]
    # Add more dates here
}

ANNIVERSARIES = {
    "26 11": [("Neelu Massi", "Parveen Masaji", FAMILY_GROUPS[1])],
    "15 06": [("Baba", "Maa", FAMILY_GROUPS[2])]
    # Add more dates here
}

def pick_emoji(lst, times=1):
    return [choice(lst) for _ in range(times)]
