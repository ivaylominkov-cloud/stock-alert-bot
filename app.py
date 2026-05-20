import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TICKERS = ["AAPL", "MSFT", "AMZN", "NVDA", "GOOGL",
           "META", "TSLA", "UNH", "XOM", "JPM"]


def send_telegram(message):
    print("Sending Telegram message...")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": message},
        timeout=10  # ✅ prevents hanging
    )

    print("Telegram status:", response.status_code)


def get_prices():
    symbols = ",".join(TICKERS)
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbols}"

