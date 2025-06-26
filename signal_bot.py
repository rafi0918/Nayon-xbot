from dotenv import load_dotenv
import os
import requests
import datetime
import pytz
import time

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

def send_signal(signal):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": signal
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ Signal sent successfully!")
        else:
            print(f"❌ Failed to send signal: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending signal: {e}")

def run_signal_loop():
    while True:
        # ✅ বাংলাদেশের টাইম
        bd_time = datetime.datetime.now(pytz.timezone('Asia/Dhaka'))

        # ✅ ১ মিনিট পরের টাইম (যখন ট্রেড নিবে)
        trade_time = (bd_time + datetime.timedelta(minutes=1)).strftime('%I:%M %p')

        signal = (
            "📈 Qatex Auto Signal\n\n"
            "🪙 Pair: USD/JPY\n"
            "🧭 Action: Sell 🔽\n"
            "🕐 Timeframe: 1 Minute\n"
            f"⏰ Trade at: {trade_time} (Bangladesh Time)\n"
            "📊 Confidence: 99%"
        )

        send_signal(signal)
        time.sleep(120)

if __name__ == "__main__":
    run_signal_loop()
