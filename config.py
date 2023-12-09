import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", 26930530))
API_HASH = os.environ.get("API_HASH", "b578cec1f4f5164d952c5a785a399a73")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6510599693:AAFxoVijOtGDcSDVmpU2XSwpRkqRqdXB9i8")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
