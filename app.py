import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Fetch Bot Token and Chat ID from Environment Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Function to send alerts to Telegram
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Will raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")

# Webhook endpoint to handle POST requests from TradingView
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        if 'ticker' in data and 'message' in data:
            message = f"📈 *Volume Spike Alert!*\n\nSymbol: `{data['ticker']}`\nMessage: {data['message']}"
        else:
            message = f"📢 Alert: {data}"  # Fallback for missing fields

        send_telegram_alert(message)
        return 'ok', 200
    else:
        return 'Invalid data', 400
