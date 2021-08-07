from lane import laneClient
from pyrogram import filters
import requests
import json
from urllib.request import urlopen

url = "https://animechan.vercel.app/api/random"

@laneClient.on_message(filters.command('quote','.') & filters.me)
async def quote(lane, message):
    respon = requests.get(url)
    data = respon.json()
    quote = data['quote']
    character = data['character']
    await message.edit(quote + ' - ' + character)
    
