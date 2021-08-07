from lane import laneClient
from pyrogram import filters

@laneClient.on_message(filters.command('help', '.') & filters.me)
async def help(lane, message):
  HELP_STRING = (
    "working on it!"
    )
  await message.edit(HELP_STRING)