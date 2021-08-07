from logging import info
from lane import laneClient
from pyrogram.errors import PeerIdInvalid
from pyrogram import filters

info = '`User info:`\n\n'
info += '**First Name:** `{}`\n'
info += '**Last Name:** `{}`\n'
info += '**Username:** @{}\n'
info += '**ID:** `{}`\n'
info += '**Profile photos count:** `{}`'

@laneClient.on_message(filters.command('info', '.') & filters.me)
async def whois(lane, message):
    cd = message.command
    if not message.reply_to_message and len(cd) == 1:
        user = message.from_user.id
        chat = message.chat.id
        pfp_count = await laneClient.get_profile_photos_count(user)
        pfp = await laneClient.get_profile_photos(user, limit=1)
        pic = pfp[0]["file_id"]
    elif len(cd) == 1:
        if message.reply_to_message.forward_from:
            user = message.reply_to_message.forward_from.id
            chat = message.chat.id
            pfp_count = await laneClient.get_profile_photos_count(user)
            pfp = await laneClient.get_profile_photos(user, limit=1)
            pic = pfp[0]["file_id"]
        else:
            user = message.reply_to_message.from_user.id
            chat = message.chat.id
            pfp_count = await laneClient.get_profile_photos_count(user)
            pfp = await laneClient.get_profile_photos(user, limit=1)
            pic = pfp[0]["file_id"]
    elif len(cd) > 1:
        user = cd[1]
        chat = message.chat.id
        pfp_count = await laneClient.get_profile_photos_count(user)
        pfp = await laneClient.get_profile_photos(user, limit=1)
        pic = pfp[0]["file_id"]
        try:
            user = int(cd[1])
        except ValueError:
            pass
    try:
        usr = await laneClient.get_users(user)
    except PeerIdInvalid:
        await message.delete()
    await laneClient.send_photo(
        chat_id=chat,
        photo=pic,
        caption=info.format(
            usr.mention,
            usr.last_name,
            usr.username,
            usr.id,
            pfp_count
        )
    )