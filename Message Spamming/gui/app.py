import tkinter as tk
from tkinter import filedialog, messagebox
from spammer.core import open_browser, select_group, send_message
from spammer.media import send_media_file
from time import sleep
from pyautogui import press

class WhatsAppSpammerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Spammer")
        self.root.geometry("500x550")

        # Website Wait Time
        tk.Label(root, text="Website Wait Time (sec):").pack()
        self.wait_time = tk.Entry(root)
        self.wait_time.pack()

        # Group Name
        tk.Label(root, text="Group/Chat Name:").pack()
        self.group_name = tk.Entry(root)
        self.group_name.pack()

        # Message Area
        tk.Label(root, text="Messages to Send (one per line):").pack()
        self.message_box = tk.Text(root, height=10)
        self.message_box.pack()

        # Repeat Count
        tk.Label(root, text="Number of Repetitions (per message):").pack()
        self.repeat_count = tk.Entry(root)
        self.repeat_count.pack()

        # Media Path (optional)
        tk.Label(root, text="Attach Media File (optional):").pack()
        self.media_path = tk.StringVar()
        tk.Entry(root, textvariable=self.media_path, state='readonly').pack()
        tk.Button(root, text="Browse", command=self.browse_file).pack()

        # Status
        self.status = tk.Label(root, text="Status: Idle", fg="blue")
        self.status.pack(pady=10)

        # Start Button
        tk.Button(root, text="Start Spamming", command=self.run_spammer).pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.media_path.set(file_path)

    def run_spammer(self):
        try:
            wait = float(self.wait_time.get())
            group = self.group_name.get()
            messages = self.message_box.get("1.0", tk.END).strip().splitlines()
            repeats = int(self.repeat_count.get())
            media_file = self.media_path.get()

            self.status.config(text="Opening WhatsApp Web...", fg="orange")
            self.root.update()
            open_browser("https://web.whatsapp.com", wait)

            self.status.config(text=f"Selecting group: {group}", fg="orange")
            self.root.update()
            select_group(group)

            for msg in messages:
                for _ in range(repeats):
                    send_message(msg)
                    press("enter")
                    sleep(0.3)

            if media_file:
                self.status.config(text=f"Sending media: {media_file}", fg="orange")
                self.root.update()
                send_media_file(media_file)

            self.status.config(text="✅ Spamming Completed", fg="green")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status.config(text="❌ Failed", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppSpammerGUI(root)
    root.mainloop()
