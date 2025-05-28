import os
from os import getenv

API_ID = int(os.environ.get("API_ID", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("8081454054:AAE8ZBREO2CSNQu391PlNHPbVFqYDyeNo70", "")

OWNER_ID = int(os.environ.get("5780489432", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
