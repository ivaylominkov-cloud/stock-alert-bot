import os
import requests

print("BOT STARTED ✅")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("Token exists:", BOT_TOKEN is not None)
print("Chat ID exists:", CHAT_ID is not None)

def send_test():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": "✅ Bot is working!"},
        timeout=10
    )
    print("Telegram response:", response.status_code)

send_test()

print("BOT FINISHED ✅")
