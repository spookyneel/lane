from lane import laneClient
import asyncio
from pyrogram import filters
from asyncio.subprocess import PIPE as async_pipe
import time
from version import __version__ as ver
from version import __name__ as n
import lane

ALIVE_IMG = 'https://imgur.com/a/Ak8xFGz'
ALIVE_STRING = (
    "`Status: Alive`\n\n`Owner`: {}\n\n`Uptime: {}`\n\n`Ping: {}`\n\n`Bot name: {}`\n\n`Bot version: {}`"
)
    
@laneClient.on_message(filters.command('alive', '.') & filters.me)
async def alive(lane, message):
  process = await asyncio.create_subprocess_shell(
    "uptime",
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE
    )
  stdout, stderr = await process.communicate()
  result = str(stdout.decode().strip()) + str(stderr.decode().strip())
  owner =  message.from_user.mention
  start_time = time.time()
  await message.edit("`Calculating latency and stats...`")
  end_time = time.time()
  ping_time = round((end_time - start_time) * 1000, 3)

  await laneClient.send_photo(
    chat_id=message.chat.id,
    photo=ALIVE_IMG,
    caption=ALIVE_STRING.format(owner, result, ping_time, n, ver)
    )
  
  # Deletion of command message
  await message.delete()


@laneClient.on_message(filters.command('stats', '.') & filters.me)
async def sysdetails(lane, message):
    try:
        neo = "neofetch --stdout"
        process = await asyncio.create_subprocess_shell(
        neo,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await process.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await message.edit("`" + result + "`")
    except FileNotFoundError:
        await message.edit("`You don't have neofetch installed.\nInstall neofetch to make this work.`")
