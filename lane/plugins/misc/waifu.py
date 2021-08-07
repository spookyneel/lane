from lane import laneClient
from pyrogram import filters
import requests
import json
from urllib.request import urlopen

url = "https://api.waifu.pics/sfw/waifu"

@laneClient.on_message(filters.command('waifu','.') & filters.me)
async def waifu(lane, message):
    respon = requests.get(url)
    data = respon.json()
    pic = data['url']

    await laneClient.send_photo(
        chat_id=message.chat.id,
        photo=pic,
    )

    await message.delete()
