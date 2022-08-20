from pyrogram import filters, Client 
from pyrogram.types import *
import os
from requests import get

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)


#logo api's
LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="

#Cilent start
pyrobot = Client("logomaker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)   
      
pyrobot.run()