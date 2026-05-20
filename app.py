import requests
import os

print("START ✅")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "Hello ✅"
    },
    timeout=10
)

print("Telegram status:", response.status_code)
print("END ✅")
