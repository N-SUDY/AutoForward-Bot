import os
from pyrogram import Client

def create_userbot_session(session_name):
    """Create a new Pyrogram userbot session."""
    api_id = int(os.environ.get("API_ID"))
    api_hash = os.environ.get("API_HASH")
    
    with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
        app.start()
        session_string = app.export_session_string()
    
    return session_string

def start_userbot_session(session_name, session_string):
    """Start a Pyrogram userbot session."""
    api_id = int(os.environ.get("API_ID"))
    api_hash = os.environ.get("API_HASH")
    
    app = Client(session_name, api_id=api_id, api_hash=api_hash)
    app.start()
    return app

def stop_userbot_session(app):
    """Stop a Pyrogram userbot session."""
    app.stop()
    