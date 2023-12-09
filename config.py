import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI")
