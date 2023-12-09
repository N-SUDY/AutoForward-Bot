from pyrogram import Client, filters
from pyrogram.types import Message

# Import your Database class and other necessary modules
from database import Database
from config import API_ID, API_HASH, USERBOT_SESSION_NAME

# Initialize the userbot client
userbot = Client(USERBOT_SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# Initialize the database
db = Database()

# Forward messages as a userbot
@userbot.on_message(filters.private & ~filters.edited)
async def forward_messages(client: Client, message: Message):
    user_id = message.chat.id
    user_settings = db.get_user_settings(user_id)

    if user_settings is None:
        await message.reply("Please set up your settings using the main bot.")
        return

    # Check if the user has a valid userbot session
    if not user_settings.get("userbot_session"):
        await message.reply("Please provide your userbot session using the main bot.")
        return

    # Check if the user is a member of the source chat (if it's a private source chat)
    if await client.get_chat_member(message.text, user_id) is None:
        await message.reply("You must be a member of the source chat to forward messages.")
        return

    # Forward the message using the userbot session
    userbot_client = Client(user_settings["userbot_session"], api_id=API_ID, api_hash=API_HASH)
    
    async with userbot_client:
        await userbot_client.forward_messages(
            user_id, message.chat.id, message.message_id
        )

if __name__ == "__main__":
    userbot.run()
    