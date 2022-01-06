import os
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv("BOT_TOKEN")
telegram_bot_username=os.getenv("BOT_USERNAME")
