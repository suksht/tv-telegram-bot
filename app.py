from flask import Flask, request
import requests

app = Flask(__name__)

# Your Bot Token and Chat ID (Replace with your actual details)
BOT_TOKEN = '7662346368:AAHlygCgzzE9Wsdm0GcG3_DShx7O5tTqBo8'  # Replace with your token
CHAT_ID = '5994456404'  # Replace with your chat ID

# Function to send Telegram alerts
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, json=payload)

# Simple home route
@app.route('/', methods=['GET'])
def home():
    return '✅ Flask app is running on Render!'

# Webhook route to receive POST requests
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', 'No message provided')
    ticker = data.get('ticker', 'No symbol')
    final_message = f"📈 Signal Alert\n\nSymbol: {ticker}\nMessage: {message}"
    
    print(f"📩 Incoming webhook: {final_message}")
    send_telegram_alert(final_message)
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
