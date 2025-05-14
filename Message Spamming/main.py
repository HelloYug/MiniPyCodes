from spammer.core import open_browser, select_group, send_message
from spammer.media import send_media_file
from pyautogui import press
from time import sleep

def main():
    try:
        wait_time = float(input("Enter website wait time (in seconds): "))
        group_name = input("Enter the Chat or Group name you want to spam: ")
        print("Enter the message(s) you want to spam (use \\n for line breaks):")
        message = input(">>> ")
        repeat_count = int(input("Enter the number of times to repeat the message: "))
        media_choice = input("Do you want to send a media file? (y/n): ").lower()

        media_path = ""
        if media_choice == "y":
            media_path = input("Enter the absolute path to the media file: ")

        print("\nOpening WhatsApp Web...")
        open_browser("https://web.whatsapp.com", wait_time)

        print(f"Selecting group: {group_name}...")
        select_group(group_name)

        for _ in range(repeat_count):
            send_message(message)
            press("enter")
            sleep(0.3)

        if media_path:
            print("Sending media...")
            send_media_file(media_path)

        print("\n✅ Spamming completed successfully.")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
