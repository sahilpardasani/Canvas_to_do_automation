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
- 🐳 Dockerized Deployment: Containerized using Docker for consistent and hassle-free deployment across different environments.
- 🛠️ Cron Integration: Scheduled execution using cron (macOS/Linux) for full automation.

---

## 🖥️ Tech Stack

- `Python 3.10+`
- [`canvasapi`](https://github.com/ucfopen/canvasapi)
- `pytz` + `tzlocal` for smart timezone detection
- `python-dotenv`
- `requests`
- `crontab` for scheduling (macOS/Linux)
- pytz & tzlocal: Handle timezone conversions and detections.
---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/sahilpardasani/canvas-whatsapp-reminder.git
cd canvas-whatsapp-reminder
```
### 2. To install dependencies
pip install -r requirements.txt

### Configure Environment Variables
Create a .env file in the root directory and add the following:
CANVAS_API_KEY=your_canvas_api_key
CALLMEBOT_API_KEY=your_callmebot_api_key
WHATSAPP_PHONE=your_whatsapp_phone_number

Or simply just create the .environment file and make sure it's in the same folder and as the Docker container and run the container
### Run the Docker Container
docker run --rm canvas-reminder-bot

