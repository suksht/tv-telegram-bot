from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', 'No message received')
    
    send_text = f"🚨 TradingView Alert:\n{message}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": send_text
    }
    requests.post(url, data=payload)
    return "OK"
