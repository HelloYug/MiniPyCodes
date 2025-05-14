
# WhatsApp Message Spammer 💬⚠️

A Python automation tool that helps you spam messages (and even media) on WhatsApp Web.

---

## 🚀 Features

- ✅ Automatically opens WhatsApp Web
- ✅ Searches for a group/contact
- ✅ Sends single or multiple messages
- ✅ Repeats messages multiple times
- ✅ Supports emojis and multi-line messages
- ✅ GUI with Tkinter for ease of use
- ✅ Optionally attach and send images or videos

---

## 🛠️ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
````



---

## 📂 Folder Structure

```
whatsapp_spammer/
├── spammer/
│   ├── core.py         # message spam logic
│   └── media.py        # media handling logic
│    
├── gui/
│   └── app.py          # Tkinter GUI
├── main.py             # CLI version
├── requirements.txt
└── README.md
```

---

## 🧪 Usage (CLI)

```bash
python main.py
```

### CLI Prompts:

1. Website wait time
2. Group or chat name
3. Message to spam
4. Number of repetitions

---

## 🖼️ Usage (GUI)

```bash
python gui/app.py
```

### GUI Features:

* Fill in group name, message(s), repeat count
* Supports multi-line messages
* Optional: Browse and attach a media file
* One-click "Start Spamming"

---

## 📷 Sending Media

Media spamming works by:

* Selecting a file via GUI
* Simulating file attachment and sending in WhatsApp Web
* Works best when WhatsApp’s attach button is already clicked

---

## ⚠️ Disclaimer

This tool is provided for **educational purposes only**.
Spamming is against WhatsApp's Terms of Service. Please use responsibly and ethically.

---

## 👨‍💻 Author

**Yug Agarwal**
- 📧 [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
- 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)
