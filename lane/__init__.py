import sys
import asyncio
from pyrogram import Client
from config import Configuration

from .anilist import AniList
from version import __version__

from pymongo import MongoClient

laneClient = Client(
  session_name=Configuration.SESSION_STRING,
  api_id=Configuration.API_ID,
  api_hash=Configuration.API_HASH,
  app_version=__version__
  )


laneBotClient = Client(
  session_name='botSession',
  api_id=Configuration.API_ID,
  api_hash=Configuration.API_HASH,
  bot_token=Configuration.PM_LOGGER_BOT_TOKEN
).start()

try:
  if Configuration.development_mode:
    laneMongo = MongoClient(Configuration.MONGO_URI).laneDeveloper
    print('MongoDB Development database server started!')
  else:
    laneMongo = MongoClient(Configuration.MONGO_URI).lane
    print('MongoDB started!')
except:
  sys.exit('MongoDB couldn\'t connect!')

anilist = AniList()

if Configuration.USER_ID is not None:
  user_data = laneMongo.settings.find_one(
        {
            'user_id': Configuration.USER_ID
        }
    )
  if user_data is None:
    laneMongo.settings.insert(
        {
            '_id': 1,
            'user_id': Configuration.USER_ID
        }
    )

    