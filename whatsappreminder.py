from canvasapi import Canvas
from dotenv import load_dotenv
import os
import requests
import urllib.parse
from datetime import datetime, timezone, timedelta
import pytz
from tzlocal import get_localzone

# === Load environment variables ===
load_dotenv(dotenv_path=".env")

API_URL = "https://psu.instructure.com"
API_KEY = os.getenv("CANVAS_API_KEY")
WHATSAPP_PHONE = os.getenv("WHATSAPP_PHONE")
CALLMEBOT_API_KEY = os.getenv("CALLMEBOT_API_KEY")

# === Validate environment ===
if not API_KEY or not WHATSAPP_PHONE or not CALLMEBOT_API_KEY:
    print("❌ Missing one or more environment variables.")
    exit(1)

# === Initialize Canvas client ===
canvas = Canvas(API_URL, API_KEY)

# === Determine your timezone ===
try:
    user = canvas.get_current_user()
    tz_name = getattr(user, 'time_zone', None)
    if not tz_name and hasattr(user, '_attributes'):
        tz_name = user._attributes.get('time_zone')
    if tz_name:
        LOCAL_TZ = pytz.timezone(tz_name)
    else:
        raise AttributeError
    print(f"🕒 Using Canvas timezone: {tz_name}")
except Exception:
    LOCAL_TZ = get_localzone()
    print(f"🕒 Falling back to system timezone: {LOCAL_TZ}")

# === WhatsApp send function ===
def send_whatsapp(message: str):
    encoded = urllib.parse.quote_plus(message)
    url = (
        f"https://api.callmebot.com/whatsapp.php"
        f"?phone={WHATSAPP_PHONE}"
        f"&text={encoded}"
        f"&apikey={CALLMEBOT_API_KEY}"
    )
    resp = requests.get(url)
    text = resp.text or ""
    if "Message Sent" in text or "queued" in text:
        print("✅ WhatsApp message sent/queued!")
    else:
        print("❌ Failed to send message.")
        print("Response:", text)

# === Fetch your Canvas To-Do list ===
todo = canvas.get_todo_items()

# === Build & send daily To-Do message ===
if not todo:
    send_whatsapp("🎉 No tasks in your Canvas To-Do list today. Time to chill!")
else:
    msg = "📝 *Your Canvas To-Do List:*\n"
    for item in todo:
        assignment = item.assignment  # assignment is a dict
        name = assignment.get("name", "Unnamed Task") if assignment else "Unnamed Task"
        course = item.context_name or "Unknown Course"
        due_utc = assignment.get("due_at") if assignment else None
        if due_utc:
            dt = datetime.fromisoformat(due_utc.replace('Z', '+00:00'))
            local = dt.astimezone(LOCAL_TZ)
            due_str = local.strftime("%Y-%m-%d %I:%M %p %Z")
        else:
            due_str = "No due date"
        msg += f"\n• {name} ({course})\n  Due: {due_str}"
    send_whatsapp(msg)

# === 1-hour-before reminders ===
now_utc = datetime.now(timezone.utc)
for item in todo:
    assignment = item.assignment  # still a dict
    due_utc = assignment.get("due_at") if assignment else None
    if due_utc:
        dt = datetime.fromisoformat(due_utc.replace('Z', '+00:00'))
        diff = dt - now_utc
        if timedelta(minutes=59) <= diff <= timedelta(minutes=61):
            name = assignment.get("name", "Unnamed Task") if assignment else "Unnamed Task"
            course = item.context_name or "Unknown Course"
            local = dt.astimezone(LOCAL_TZ)
            remind_at = local.strftime("%Y-%m-%d %I:%M %p %Z")
            reminder = f"⏰ *Reminder:* '{name}' from {course} is due in 1 hour at {remind_at}."
            send_whatsapp(reminder)
