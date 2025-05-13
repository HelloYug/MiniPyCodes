from datetime import datetime
from time import time

LOG_PATH = "E:\\Yug's Storage\\Desktop\\Yug Study\\Programming\\CS Python\\Yug's Major Projects\\Whatsapp Greeting\\Log Files\\"

def log_wish(kind, name, group, start_time):
    with open(f"{LOG_PATH}WishWhatsAppLogFile.txt", "a") as f:
        timestamp = datetime.now().strftime("%H:%M:%S %d-%m-%Y (%a)")
        f.write(f"\nTime : {timestamp}")
        f.write(f"\n\tMessage Type : Wishing {kind} to {name}")
        f.write(f"\n\tChat Name    : {group}")
        f.write(f"\n\tTime taken   : {round(time() - start_time, 4)} Seconds")
        f.write("\n" + "-" * 60)

def log_greeting(count, start_time):
    with open(f"{LOG_PATH}GreetWhatsAppLogFile.txt", "a") as f:
        timestamp = datetime.now().strftime("%H:%M:%S %d-%m-%Y (%a)")
        f.write(f"\nTime : {timestamp}")
        f.write(f"\n\tGroups Wished : {count}")
        f.write(f"\n\tTime taken    : {round(time() - start_time, 4)} Seconds")
        f.write("\n" + "-" * 40)
