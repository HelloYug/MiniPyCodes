from datetime import datetime, timedelta
from time import sleep, time
from greetings.messenger import open_whatsapp, send_greeting, close_tab
from greetings.data import FAMILY_GROUPS, FRIENDS_GROUPS, FAMILY_MESSAGES, FRIENDS_MESSAGES, FLOWERS, HEARTS, BIRTHDAYS, ANNIVERSARIES, pick_emoji
from greetings.log import log_greeting, log_wish

next_morning = (datetime.now() + timedelta(seconds=7)).strftime("%H %M %S")
next_event = "00 05 00"

def run_greetings():
    while True:
        now = datetime.now().strftime("%H %M %S")

        if now == next_morning:
            st = time()
            open_whatsapp(18)
            count = 0

            for g in FAMILY_GROUPS:
                msg = pick_emoji(FAMILY_MESSAGES)[0]
                emoji = "🦚" if msg == "Radhe radhe " else "🙏"
                send_greeting(g, msg, emoji)
                send_greeting(g, "", pick_emoji(FLOWERS)[0])
                count += 1

            for g in FRIENDS_GROUPS:
                msg = pick_emoji(FRIENDS_MESSAGES)[0]
                send_greeting(g, msg, pick_emoji(HEARTS if msg == "Mornaa!! " else FLOWERS)[0])
                count += 1

            close_tab()
            log_greeting(count, st)

        if now == next_event:
            today = datetime.now().strftime("%d %m")
            if today in ANNIVERSARIES:
                for n1, n2, g in ANNIVERSARIES[today]:
                    st = time()
                    open_whatsapp(10)
                    send_greeting(g, f"Happy Anniversary {n1} and {n2} ", pick_emoji(HEARTS)[0])
                    send_greeting(g, "Wish you many many more years together!", "🥳")
                    close_tab()
                    log_wish("Anniversary", f"{n1} & {n2}", g, st)

            if today in BIRTHDAYS:
                for name, g in BIRTHDAYS[today]:
                    st = time()
                    open_whatsapp(10)
                    send_greeting(g, f"Happy Birthday {name} 🥳", pick_emoji(HEARTS)[0])
                    send_greeting(g, "Many many happy returns of the Day! ", "🎉")
                    close_tab()
                    log_wish("Birthday", name, g, st)

        sleep(1)
