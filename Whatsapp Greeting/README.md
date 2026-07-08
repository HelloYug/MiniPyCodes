# 🙋‍♂️ WhatsApp Auto-Greeter

This project automates daily greetings and special occasion wishes (birthdays and anniversaries) to family and friend WhatsApp groups using Python and `pyautogui`.

---

## 🚀 Features
- Sends **morning greetings** to multiple WhatsApp groups.
- Automatically sends **birthday** and **anniversary** wishes on specific dates.
- Includes **emojis** and **message customization**.
- Logs every message sent with timestamps.

---

## 🛠 Requirements
- Python 3.7+
- Modules:
  ```bash
  pip install pyautogui pyperclip
  ```
- Desktop browser (default used via `webbrowser.open`)
- WhatsApp Web must be logged in and stable internet connection

---

## 📂 Project Structure
```
whatsapp_greeter/
├── greetings/
│   ├── data.py           # Group names, greetings, emoji sets, dates
│   ├── messenger.py      # WhatsApp automation functions
│   ├── log.py            # Logging of greetings and events
│   └── scheduler.py      # Time-check loop and action triggers
│
├── main.py               # Entry point to run the automation
└── README.md             # Project documentation
```

---

## ⏱ How It Works
- The scheduler checks time every second.
- When time matches `next_morning` or `next_event`, it triggers greetings.
- It uses `pyautogui` to control the keyboard/mouse and send messages.

---

## 🧪 Usage
1. Open your terminal and navigate to the project folder.
2. Run the script:
   ```bash
   python main.py
   ```
3. Leave your system on. Messages will be sent at the configured time automatically.

---

## ⚠️ Notes
- Do not move the mouse/keyboard while it's sending messages.
- Make sure your screen isn't locked.
- You can customize dates, messages, and groups in `data.py`

---

## 👨‍💻 Author

**Yug Agarwal**

* 📧 Email – [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
* 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)
* 💼 LinkedIn – [yugagarwal704](https://www.linkedin.com/in/yugagarwal704/)
* 🌐 Portfolio – [yugagarwal.dev](https://yugagarwal.dev/?utm_source=github&utm_medium=readme&utm_campaign=MiniPyCodes_readme)