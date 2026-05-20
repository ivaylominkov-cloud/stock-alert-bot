import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TICKERS = ["AAPL", "MSFT", "AMZN", "NVDA", "GOOGL",
           "META", "TSLA", "UNH", "XOM", "JPM"]


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })


def get_prices():
    symbols = ",".join(TICKERS)
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbols}"

    response = requests.get(url)
    data = response.json()

    results = data["quoteResponse"]["result"]

    messages = []

    for stock in results:
        symbol = stock["symbol"]
        price = stock.get("regularMarketPrice", None)

        if price:
            messages.append(f"{symbol}: ${price:.2f}")

    return messages


def main():
    print("Checking prices...")

    try:
        prices = get_prices()

        if prices:
