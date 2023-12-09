from pymongo import MongoClient
from config import MONGODB_URI

class Database:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client.get_database()

    def add_user(self, user_id):
        user = {
            "user_id": user_id,
            "settings": {
                "target_channels": [],
                "custom_caption": "",
                "filters": {},
                "custom_button": "",
                "dummy_bot_token": "",
                "userbot_session": "",
            },
        }
        self.db.users.insert_one(user)

    def get_user_settings(self, user_id):
        user = self.db.users.find_one({"user_id": user_id})
        if user:
            return user["settings"]
        else:
            return None

    def update_user_settings(self, user_id, settings):
        self.db.users.update_one({"user_id": user_id}, {"$set": {"settings": settings}})

    def get_users_with_target_channels(self, target_channel_id):
        users = self.db.users.find({"settings.target_channels": target_channel_id})
        return [user["user_id"] for user in users]

    def close(self):
        self.client.close()
        