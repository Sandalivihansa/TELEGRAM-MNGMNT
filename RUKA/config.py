


import os
import json


def get_user_list(key):
    with open("users.json", "r") as json_file:
        return json.load(json_file)[key]


class Config:
    # Basic Bot Configuration
    TOKEN = os.getenv("TOKEN", "7332398186:AAHG5L3MF-8BtP4ouR_9a_T2tBgje_GegN0")
    API_ID = int(os.getenv("API_ID", 5047271))
    API_HASH = os.getenv("API_HASH", "047d9ed308172e637d4265e1d9ef0c27")
    BOT_USERNAME = os.getenv("BOT_USERNAME", "testingplate45_bot")

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "https://blue-api.vercel.app/database?client=ishikki@xyz242.gramdb")

    # Logging and Monitoring
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002325247996"))  # Example: -1001234567890 (Private Channel ID)
    ERROR_LOG_CHANNEL = int(os.getenv("ERROR_LOG_CHANNEL", -1002325247996))
   
    # Access Control
    DEV_USERS = list(map(int, os.getenv("DEV_USERS", "1451534504").split(',')))
    OWNER_ID = int(os.getenv("OWNER_ID", 1451534504))

    # Optional Extras
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "hghgjkgjgjk")  # Without '@'
    SUPPORT_CHAT_ID = int(os.getenv("SUPPORT_CHAT_ID", -1001720451925))
    
    # Additional API integrations
    MEOWCORE_TOKEN = os.getenv("MEOWCORE_TOKEN", "69696969-MeowMeow")
