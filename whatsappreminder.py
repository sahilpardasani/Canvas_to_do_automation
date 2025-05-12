from canvasapi import Canvas
from dotenv import load_dotenv
import os
import requests
import urllib.parse

# Load environment variables
load_dotenv(dotenv_path=".env")

# Canvas setup
API_URL = "https://psu.instructure.com"
API_KEY = os.getenv("CANVAS_API_KEY")
canvas = Canvas(API_URL, API_KEY)

# CallMeBot setup
WHATSAPP_PHONE = os.getenv("WHATSAPP_PHONE")
CALLMEBOT_API_KEY = os.getenv("CALLMEBOT_API_KEY")

# Check for required environment variables
if not API_KEY or not WHATSAPP_PHONE or not CALLMEBOT_API_KEY:
    print("❌ Missing one or more environment variables.")
    exit(1)

# === TO-DO LIST SECTION ===
todo_items = canvas.get_todo_items()

# Format message
if not todo_items:
    message = "🎉 No tasks in your Canvas To-Do list!"
else:
    message = "📝 *Your Canvas To-Do List:*\n"
    for item in todo_items:
        name = item['assignment']['name']
        course = item['context_name']
        due = item['assignment'].get('due_at', 'No due date')
        message += f"\n• {name} ({course})\n  Due: {due}"

# Encode and send via CallMeBot
encoded_msg = urllib.parse.quote_plus(message)
url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_PHONE}&text={encoded_msg}&apikey={CALLMEBOT_API_KEY}"

response = requests.get(url)

# Feedback
if "Message Sent" in response.text:
    print("✅ WhatsApp message sent successfully!")
else:
    print("❌ Failed to send message.")
    print("Response:", response.text)
