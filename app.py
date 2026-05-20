import requests
import yfinance as yf
import os

# Get secrets from GitHub
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


def check_prices():
    print("Checking prices...")

    try:
        # ✅ FAST: fetch all stocks in one request
        data = yf.download(
            tickers=TICKERS,
            period="1d",
            interval="1m",
            group_by="ticker",
            threads=True
        )

        messages = []

        for ticker in TICKERS:
            try:
                price = data[ticker]["Close"].iloc[-1]
                messages.append(f"{ticker}: ${price:.2f}")
            except Exception as e:
                print(f"Error with {ticker}: {e}")

        # ✅ send one clean message instead of spam
        if messages:
            full_message = "📊 Stock Prices:\n\n" + "\n".join(messages)
            send_telegram(full_message)

    except Exception as e:
        print("Download error:", e)


# ✅ IMPORTANT: run once (NO while loop!)
if __name__ == "__main__":
    check_prices()
``
