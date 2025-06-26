from flask import Flask, request
from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import pytz

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data:
        pair = data.get("pair")
        action = data.get("action")
        
        # Bangladesh time
        bd_time = datetime.now(pytz.timezone("Asia/Dhaka")).strftime("%I:%M %p")
        
        signal = {
            "pair": pair,
            "action": action
        }
        send_signal(signal, bd_time)
        return "Signal sent!", 200
    return "No data", 400

def send_signal(signal, trade_time):
    message = f"""📈 Qatex Auto Signal

🪙 Pair: {signal['pair']}
🧭 Action: {signal['action']} {'🔼' if signal['action'].lower() == 'buy' else '🔽'}
🕐 Timeframe: 1 Minute
📊 Confidence: 99%
⏰ Trade Time: {trade_time} (BD Time)
⚠️ Enter trade within 30 seconds on Qatex!
"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
