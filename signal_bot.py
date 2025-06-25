import requests
import time


chat_id = "5758714029"

def get_signal():
    # Example: Dummy signal generator
    import random
    pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USDT", "ETH/USDT"]
    signal = random.choice(["BUY", "SELL"])
    pair = random.choice(pairs)
    return f"{pair} → {signal}"

def send_signal(signal):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": signal
    }
    requests.post(url, data=payload)

while True:
    signal = get_signal()
    send_signal(signal)
    time.sleep(120)  # every 2 minutes
