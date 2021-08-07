from lane import laneClient
from pyrogram import filters
from lane.helper.get_user import get_user

@laneClient.on_message(filters.command('id', '.') & filters.me)
async def id(lane, message):
    id = await get_user(message)
    await message.edit('**Username:** @{}\n**User ID:** `{}`'.format(id['username'], id['id']))

@laneClient.on_message(filters.command('chatid', '.') & filters.me)
async def chatid(lane, message):
    id = message.chat.id
    await message.edit('**Chat ID:** `{}`'.format(id))    