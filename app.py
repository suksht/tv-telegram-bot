import requests
from flask import Flask, request

app = Flask(__name__)

# Your Telegram Bot Token and Chat ID
BOT_TOKEN = '7662346368:AAHlygCgzzE9Wsdm0GcG3_DShx7O5tTqBo8'
CHAT_ID = '5994456404'

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
        # Check if the necessary data is present and format the message
        if 'ticker' in data and 'message' in data:
            message = f"📈 *Volume Spike Alert!*\n\nSymbol: `{data['ticker']}`\nMessage: {data['message']}"
        else:
            message = f"📢 Alert: {data}"  # Fallback for missing fields

        # Send the message to Telegram
        send_telegram_alert(message)
        return 'ok', 200
    else:
        return 'Invalid data', 400

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
