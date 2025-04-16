import requests
from flask import Flask, request

app = Flask(__name__)

# Replace with your Telegram bot token and your chat ID
BOT_TOKEN = '7662346368:AAHlygCgzzE9Wsdm0GcG3_DShx7O5tTqBo8'
CHAT_ID = '5994456404'

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot7662346368:AAHlygCgzzE9Wsdm0GcG3_DShx7O5tTqBo8/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'ticker' in data and 'message' in data:
        message = f"📈 *Volume Spike Alert!*\n\nSymbol: `{data['ticker']}`\nMessage: {data['message']}"
    else:
        message = f"📢 Alert: {data}"
    send_telegram_alert(message)
    return 'ok', 200

if __name__ == '__main__':
    app.run(port=5000)
