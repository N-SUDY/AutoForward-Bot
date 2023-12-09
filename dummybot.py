from pyrogram import Client, filters
from pyrogram.types import Message

# Import your Database class and other necessary modules
from database import Database
from config import API_ID, API_HASH, DUMMYBOT_TOKEN

# Initialize the dummy bot client
dummybot = Client("dummybot", bot_token=DUMMYBOT_TOKEN)

# Initialize the database
db = Database()

# Forward messages as a dummy bot
@dummybot.on_message(filters.private & ~filters.edited)
async def forward_messages(client: Client, message: Message):
    user_id = message.chat.id
    user_settings = db.get_user_settings(user_id)

    if user_settings is None:
        await message.reply("Please set up your settings using the main bot.")
        return

    # Check if the user is a member of the source chat (if it's a private source chat)
    if await client.get_chat_member(message.text, user_id) is None:
        await message.reply("You must be a member of the source chat to forward messages.")
        return

    # Forward the message using the dummy bot
    dummybot_client = Client("dummybot", bot_token=DUMMYBOT_TOKEN)
    
    async with dummybot_client:
        await dummybot_client.forward_messages(
            user_settings["destination_chat"], message.chat.id, message.message_id
        )

if __name__ == "__main__":
    dummybot.run()
    