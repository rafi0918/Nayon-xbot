import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

def send_qatex_signal(pair="USD/JPY", action="Sell", timeframe="1 Minute", confidence="99%"):
    message = (
        "📈 Qatex Auto Signal\n\n"
        f"🪙 Pair: {pair}\n"
        f"🧭 Action: {action} {'🔽' if action.lower() == 'sell' else '🔼'}\n"
        f"🕐 Timeframe: {timeframe}\n"
        f"📊 Confidence: {confidence}"
    )
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("✅ Signal sent successfully!")
    else:
        print(f"❌ Failed to send signal. Status code: {response.status_code}")

while True:
    send_qatex_signal()
    time.sleep(120)  # ২ মিনিট ইন্টারভালে সিগন্যাল পাঠাবে
