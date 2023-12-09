import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN
from helpers import (
    start_message,
    help_message,
    forward_messages,
    private_forward_messages,
    unequify_messages,
    settings_message,
    stop_message,
    reset_message,
)

# Initialize the Pyrogram Client
bot = Client("forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Logging Configuration
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Forward Bot Start Command
@bot.on_message(filters.command("start"))
async def start(_, message):
    await start_message(bot, message)

# Forward Bot Help Command
@bot.on_message(filters.command("help"))
async def help(_, message):
    await help_message(bot, message)

# Forward Bot Forward Command
@bot.on_message(filters.command("forward"))
async def forward(_, message):
    await forward_messages(bot, message)

# Forward Bot Private Forward Command
@bot.on_message(filters.command("private_forward"))
async def private_forward(_, message):
    await private_forward_messages(bot, message)

# Forward Bot Unequify Command
@bot.on_message(filters.command("unequify"))
async def unequify(_, message):
    await unequify_messages(bot, message)

# Forward Bot Settings Command
@bot.on_message(filters.command("settings"))
async def settings(_, message):
    await settings_message(bot, message)

# Forward Bot Stop Command
@bot.on_message(filters.command("stop"))
async def stop(_, message):
    await stop_message(bot, message)

# Forward Bot Reset Command
@bot.on_message(filters.command("reset"))
async def reset(_, message):
    await reset_message(bot, message)

# Start the Bot
if __name__ == "__main__":
    bot.run()
    