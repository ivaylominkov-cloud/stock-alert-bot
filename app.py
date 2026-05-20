import time
import requests
import yfinance as yf
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TICKERS = ["AAPL", "MSFT", "AMZN", "NVDA", "GOOGL",
           "META", "TSLA", "UNH", "XOM", "JPM"]

THRESHOLD = -0.5  # percent drop
CHECK_INTERVAL = 300  # 5 minutes

previous_prices = {}


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def check_prices():
    print("Checking prices...")

    for ticker in TICKERS:
        try:
            data = yf.Ticker(ticker)
            history = data.history(period="1d", interval="1m")

            if history.empty:
                continue

            price = history["Close"].iloc[-1]

            if ticker in previous_prices:
                old_price = previous_prices[ticker]
                change = ((price - old_price) / old_price) * 100

                if change <= THRESHOLD:
                    msg = f"🔻 {ticker} dropped {change:.2f}%\nPrice: ${price:.2f}"
                    send_telegram(msg)

            previous_prices[ticker] = price

        except Exception as e:
            print(f"Error with {ticker}: {e}")


if __name__ == "__main__":
    while True:
        import requests
import yfinance as yf
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TICKERS = ["AAPL", "MSFT", "AMZN", "NVDA", "GOOGL",
           "META", "TSLA", "UNH", "XOM", "JPM"]

THRESHOLD = -0.5

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def check_prices():
    previous_prices = {}

    for ticker in TICKERS:
        try:
            data = yf.Ticker(ticker)
            history = data.history(period="1d", interval="1m")

            if history.empty:
                continue

            price = history["Close"].iloc[-1]

            if ticker in previous_prices:
                old_price = previous_prices[ticker]
                change = ((price - old_price) / old_price) * 100

                if change <= THRESHOLD:
                    msg = f"🔻 {ticker} dropped {change:.2f}%\nPrice: ${price:.2f}"
                    send_telegram(msg)

            previous_prices[ticker] = price

        except Exception as e:
            print(f"Error with {ticker}: {e}")


if __name__ == "__main__":
    check_prices()
