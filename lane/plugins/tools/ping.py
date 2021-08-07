
from lane import laneClient
from pyrogram import filters
from datetime import datetime

@laneClient.on_message(filters.command('ping', '.') & filters.me)
async def ping(lane, message):
  start = datetime.now()
  await message.edit(text="`Calculating...`")
  end = datetime.now()
  ms = (end - start).microseconds / 1000
  ping = f"**Pong:** `{ms}`"
  await message.edit(ping)
