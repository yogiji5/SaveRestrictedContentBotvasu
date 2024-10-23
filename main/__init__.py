from pyrogram import Client
from telethon.sync import TelegramClient
import logging, time, sys

# Set up logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Variables
API_ID = 23080322
API_HASH = 'b3611c291bf82d917637d61e4a136535'
BOT_TOKEN = '7096314428:AAG-JSo5pi2VTU-i1bNSsKk_Jkjt2dsZoBE'
SESSION = 'BAFgLYIAPwR4P_tICKd2uf_etLU02a2_hu8bWsFaMRjqM9rtNVj28wUUCXdSWC7bRUpQZhcwf0BULgg7LIjiZpHGJXCXqA9EUAVl02DZavQhWqJaB2IilNdgqIwsXOw1huHuL3dUU2vqf4vDXzLvOrTZvbvfi5gJk9oLd3f7ycbm2zK0CRHpvkTzN_iWCqnjgbZRWSI6L9OG4R6qeKM0K_QUyAcQlP2SwI7vEwHgCdIwhgh_3_rmUdESx-2fpj5-4heI8hnNw4nDpUGXrBSdHrqkMBCBh1aVQEdVWrAyJ-e_HyCn1Twe-4El3RQ-sh7rFxIfSM5G8zZEKDph_DXTkstu1JFB7QAAAAGCggAWAA'
FORCESUB = 'Bhupendra_Jogi_Enodes'
AUTH = 5500868603

# Initialize the bot
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID)

# Start userbot
try:
    userbot.start()
except Exception as e:
    print(f"Userbot Error: {e}")
    sys.exit(1)

# Initialize and start the main bot
Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(f"Bot Error: {e}")
    sys.exit(1)
