import html
from lane import laneClient
from pyrogram import filters

@laneClient.on_message(filters.command('adminlist', '.') & filters.me)
async def adminlist(lane, message):
    chat_title = message.chat.title 
    chat_id = message.chat.id 

    data_list = await laneClient.get_chat_members(
        chat_id=chat_id,
        filter='administrators'
        )
    ADMINS_LIST = []
    for user in data_list:
        if not user.user.is_bot:
         if user.user.username is not None:
            ADMINS_LIST.append(f'• <a href=tg://user?id={user.user.username}>{user.user.first_name}</a> - (**ID:** `{user.user.id}`)\n')
         else:
            ADMINS_LIST.append(f'• <a href=tg://user?id={user.user.id}>{user.user.first_name}</a> - (**ID:** `{user.user.id})`\n')


    admin_header = f"**Admins in {html.escape(chat_title)}:**\n\n"
    
    for admin in ADMINS_LIST:
        admin_header += admin
    await message.edit(
        (
            f"{admin_header}"
        )
    )        