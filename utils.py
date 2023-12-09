import re
import logging
from typing import List
from pyrogram.types import Message
from pyrogram import Client

# Initialize a logger
logger = logging.getLogger(__name__)

# Function to extract media captions
def extract_caption(message: Message) -> str:
    caption = message.caption if message.caption else ""
    return caption

# Function to extract buttons from a message
def extract_buttons(message: Message) -> List[List[str]]:
    buttons = []
    if message.reply_markup:
        for row in message.reply_markup.rows:
            button_row = []
            for button in row.buttons:
                if button.url:
                    button_row.append(f"[{button.text}]({button.url})")
                elif button.callback_data:
                    button_row.append(f"[{button.text}](callback_data:{button.callback_data})")
                else:
                    button_row.append(button.text)
            buttons.append(button_row)
    return buttons

# Function to filter messages based on settings
def filter_message(message: Message, settings: dict) -> bool:
    # Filter by message type (text, document, video, etc.)
    if settings.get("filter_type", ""):
        if message.media:
            if message.photo and "photo" in settings["filter_type"]:
                return True
            if message.document and "document" in settings["filter_type"]:
                return True
            if message.video and "video" in settings["filter_type"]:
                return True
            if message.audio and "audio" in settings["filter_type"]:
                return True
            if message.voice and "voice" in settings["filter_type"]:
                return True
            if message.animation and "animation" in settings["filter_type"]:
                return True
        elif message.text and "text" in settings["filter_type"]:
            return True

    # Filter by keywords
    keywords = settings.get("filter_keywords", [])
    for keyword in keywords:
        if re.search(rf'\b{re.escape(keyword)}\b', message.text, re.IGNORECASE):
            return True

    # Filter by file size
    if settings.get("filter_max_file_size", 0) > 0:
        if message.document:
            if message.document.file_size > settings["filter_max_file_size"] * 1024 * 1024:
                return False

    return False

# Function to log messages with sensitive data removed
def log_message(message: Message):
    # Filter out sensitive information like API keys or tokens
    filtered_text = re.sub(r'(token|api_key)=\S+', r'\1=FILTERED', message.text)
    logger.info(f"Received message from {message.chat.id}: {filtered_text}")

# Function to check if a message is a duplicate
async def is_duplicate_message(client: Client, chat_id: int, message_id: int) -> bool:
    try:
        message = await client.get_messages(chat_id, message_ids=message_id)
        return message is not None
    except Exception as e:
        logger.error(f"Error checking duplicate message: {e}")
        return False
        