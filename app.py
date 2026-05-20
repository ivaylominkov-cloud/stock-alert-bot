import os

print("✅ SCRIPT STARTED")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("Token exists:", BOT_TOKEN is not None)
print("Chat ID exists:", CHAT_ID is not None)

print("✅ SCRIPT FINISHED")
