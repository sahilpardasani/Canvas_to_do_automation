# 📚 Canvas WhatsApp To-Do Reminder

A Python automation tool that sends your **daily Canvas To-Do list** directly to your **WhatsApp** via [CallMeBot](https://www.callmebot.com/). Designed to keep you updated on assignment due dates, without needing to log in to Canvas manually.

---

## 🚀 Features

- ✅ Fetches upcoming assignments from **favorited Canvas courses**
- 📅 Sends a **WhatsApp message every day at 7:00 AM**
- 🛠️ Fully automated using a **cron job** on macOS
- 🔐 Loads secrets securely using a `.env` file

---

## 🖥️ Tech Stack

- `Python 3.10+`
- [`canvasapi`](https://github.com/ucfopen/canvasapi)
- [`CallMeBot`](https://www.callmebot.com/)
- `dotenv` for secure config
- `crontab` (macOS/Linux) for task scheduling

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/sahilpardasani/canvas-whatsapp-reminder.git
   cd canvas-whatsapp-reminder

Create a .env file:
CANVAS_API_KEY=your_canvas_token_here
WHATSAPP_PHONE=+(country code)xxxxxxxxxx
CALLMEBOT_API_KEY=your_callmebot_key_here

Authorize CallMeBot:
Send this on WhatsApp to +34 603 21 25 97
I allow callmebot to send me messages

Schedule with Cron (macOS/Linux)
To run the reminder every day at 7 AM: 
crontab -e
# Replace the paths below with your own virtual environment and script paths:
0 7 * 5-12 * /path/to/venv/bin/python /path/to/project/whatsappreminder.py


