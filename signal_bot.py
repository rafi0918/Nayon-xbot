from dotenv import load_dotenv
import os
import requests

# .env ফাইল লোড করা
load_dotenv()

# .env থেকে token আর chat_id নেওয়া
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

# সিগনাল পাঠানোর ফাংশন
def send_signal(signal):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": signal
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("✅ Signal sent successfully!")
    else:
        print("❌ Failed to send signal:", response.text)

# এখানে তোমার সিগনাল লিখো
signal = "🔔 Auto Signal: BUY EUR/USD for 2 minutes"

# সিগনাল পাঠাও
send_signal(signal)
