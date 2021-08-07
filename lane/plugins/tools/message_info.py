from lane import laneClient
from pyrogram import filters

@laneClient.on_message(filters.command('gm', '.') & filters.me)
async def ping(lane, message):
  print(message)
  await message.edit(message)