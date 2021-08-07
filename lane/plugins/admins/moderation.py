import time

from pyrogram.types.user_and_chats import user
from lane import laneClient
from pyrogram import filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.errors import (
    UsernameInvalid,
    ChatAdminRequired,
    PeerIdInvalid
)
from lane.helper.get_data import admin_check, get_reason, get_text
from lane.helper.time_checker import get_time, check_time, time_string_helper
from lane.helper.convert import convert_time

MUTE_PERMISSIONS = ChatPermissions(
    can_send_messages=False
)

UNMUTE_PERMISSIONS = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True
)

@laneClient.on_message(filters.command('ban', '.') & filters.me)
async def ban(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_ban = await admin_check(message)
        reason = get_reason(message)

        if can_ban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id 

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id    

            except IndexError:
                await message.edit('`Who to ban bruh?`')
                return
            
            if user_id:
                try:
                    await message.edit('`Banning...`')
                    usr = await laneClient.get_users(user_id)
                    await laneClient.kick_chat_member(chat, user_id)
                    if reason:
                        await message.edit('`Banned:` {}\n**Reason:** `{}`'.format(usr.mention, reason))
                    else:
                        await message.edit('`Banned:` {}\n**Reason:** {}'.format(usr.mention, '`None`'))

                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete()           

@laneClient.on_message(filters.command('unban', '.') & filters.me)
async def unban(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_unban = await admin_check(message)
        reason = get_reason(message)

        if can_unban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id
    
            except IndexError:
                await message.edit('`Who to unban bruh?`')
                return
            
            if user_id:
                try:
                    await message.edit('`Unbanning...`')
                    usr = await laneClient.get_users(user_id)
                    await laneClient.unban_chat_member(chat, user_id)
                    if reason:
                        await message.edit('`Unbanned:` {}\n**Reason:** `{}`'.format(usr.mention, reason))
                    else:
                        await message.edit('`Unbanned:` {}\n**Reason:** `{}`'.format(usr.mention, '`None`'))
                
                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete() 


@laneClient.on_message(filters.command('kick', '.') & filters.me)
async def kick(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_kick = await admin_check(message)
        reason = get_reason(message)

        if can_kick:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id

            except IndexError:
                await message.edit('`Who to kick bruh?`')
                return
            
            if user_id:
                try:
                    await message.edit('`Kicking...`')
                    usr = await laneClient.get_users(user_id)
                    await laneClient.kick_chat_member(chat, user_id)
                    await laneClient.unban_chat_member(chat, user_id)
                    if reason:
                        await message.edit('`Kicked:` {}\n**Reason:** `{}`'.format(usr.mention, reason))
                    else:
                        await message.edit('`Kicked:` {}\n**Reason:** {}'.format(usr.mention, '`None`'))

                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete() 

@laneClient.on_message(filters.command('mute', '.') & filters.me)
async def mute(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_mute = await admin_check(message)
        reason = get_reason(message)

        if can_mute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    reason = message.command[1]

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id
                    reason = message.command[2]

            except IndexError:
                await message.edit('`Who to mute bruh?`')
                return
            
            if user_id:
                try:
                    await message.edit('`Muting...`')
                    usr = await laneClient.get_users(user_id)
                    await laneClient.restrict_chat_member(
                        chat,
                        user_id,
                        MUTE_PERMISSIONS
                    )
                    
                    if reason:
                        await message.edit('`Muted:` {}\n**Reason:** `{}`'.format(usr.mention, reason))
                    else:
                        await message.edit('`Muted:` {}\n**Reason:** {}'.format(usr.mention, '`None`'))

                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete()

@laneClient.on_message(filters.command('unmute', '.') & filters.me)
async def unmute(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_unmute = await admin_check(message)
        reason = get_reason(message)

        if can_unmute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id

            except IndexError:
                await message.edit('`Who to unmute bruh?`')
                return
            
            if user_id:
                try:
                    await message.edit('`Unmuting...`')
                    usr = await laneClient.get_users(user_id)
                    await laneClient.restrict_chat_member(
                        chat,
                        user_id,
                        UNMUTE_PERMISSIONS
                    )
                    
                    if reason:
                        await message.edit('`Unmuted:` {}\n**Reason:** `{}`'.format(usr.mention, reason))
                    else:
                        await message.edit('`Unmuted:` {}\n**Reason:** {}'.format(usr.mention, '`None`'))

                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete()

@laneClient.on_message(filters.command('tban', '.') & filters.me)
async def tban(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_ban = await admin_check(message)
        if can_ban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id 

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id    

            except IndexError:
                await message.edit('`Who to ban bruh?.`')
                return
            
            if user_id:
                try:
                    await message.edit('`Banning...`')
                    usr = await laneClient.get_users(user_id)
                    time_args = await get_time(message)
                    print('time_arg', time_args)
                    if time_args:
                        cal_time = convert_time(int(time_args[:-1]), time_args[-1])
                        until_time = int(time.time() + int(cal_time))
                        await laneClient.kick_chat_member(
                            chat_id=chat,
                            user_id=user_id,
                            until_date=until_time
                        )

                        time_limit, time_format = time_string_helper(time_args)

                        text = f"`Banned: `{usr.mention}\n**For:** `{time_limit}` `{time_format}`\n"
                        raw_reason = get_text(message)
                        reason = ' '.join(raw_reason.split()[1:])
                        if reason:
                            text += f"**Reason**: `{reason}`"
                        else:
                            text += f"**Reason**: `None`"
                        
                        await message.edit(text)    

                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return    

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete()

@laneClient.on_message(filters.command('tmute', '.') & filters.me)
async def tmute(lane, message):
    if message.chat.type in ['group', 'supergroup']:
        chat = message.chat.id
        can_mute = await admin_check(message)

        if can_mute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id 

                else:
                    usr = await laneClient.get_users(message.command[1])
                    user_id = usr.id    

            except IndexError:
                await message.edit('`Who to mute bruh?.`')
                return
            
            if user_id:
                try:
                    await message.edit('`Muting...`')
                    usr = await laneClient.get_users(user_id)
                    time_args = await get_time(message)
                    if time_args:
                        cal_time = convert_time(int(time_args[:-1]), time_args[-1])
                        until_time = int(time.time() + int(cal_time))
                        await laneClient.restrict_chat_member(
                        chat,
                        user_id,
                        MUTE_PERMISSIONS,
                        until_date=until_time
                    )

                        time_limit, time_format = time_string_helper(time_args)
                        

                        text = f"`Muted: `{usr.mention}\n**For:** `{time_limit}` `{time_format}`\n"
                        raw_reason = get_text(message)
                        reason = ' '.join(raw_reason.split()[1:])
                        if reason:
                            text += f"**Reason**: `{reason}`"
                        else:
                            text += f"**Reason**: `None`"
                        
                        await message.edit(text)    

                except UsernameInvalid:
                    await message.edit('`Invalid username bozo`') 
                    return
              
                except PeerIdInvalid:
                    await message.edit('`Invalid ID bozo`')
                    return    
            
                except ChatAdminRequired:
                    await message.edit('`Sad shit, boozo doesn\'t have enough perms to ban an user`')
                    return

                except Exception as e:
                    await message.edit(f'`Some shit happened...`\n**Log:** `{e}`')
                    return    

        else:
            await message.edit('`Bozo, you don\'t have enough permissions`')
            return
    else:
        await message.delete()