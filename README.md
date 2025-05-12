# 📚 Canvas WhatsApp To-Do Reminder

A Python automation tool that sends your **daily Canvas To-Do list** directly to your **WhatsApp** via [CallMeBot](https://www.callmebot.com/). Designed to keep you updated on assignment due dates — no need to log in manually.

---

## 🚀 Features

- ✅ Fetches upcoming assignments from **favorited Canvas courses**
- ⏰ Sends a **WhatsApp message daily at 7:00 AM**
- 🔔 Sends an **additional reminder exactly 1 hour before** each assignment is due
- 🌍 Automatically detects your **Canvas-set timezone** or falls back to your **system timezone**
- 🛠️ Fully automated via `cron` (macOS/Linux)
- 🔐 Secure configuration via `.env` file

---

## 🖥️ Tech Stack

- `Python 3.10+`
- [`canvasapi`](https://github.com/ucfopen/canvasapi)
- `pytz` + `tzlocal` for smart timezone detection
- `python-dotenv`
- `requests`
- `crontab` for scheduling (macOS/Linux)

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/sahilpardasani/canvas-whatsapp-reminder.git
cd canvas-whatsapp-reminder
```
### 2. To install dependencies
pip install -r requirements.txt
