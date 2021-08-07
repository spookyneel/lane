from enum import Enum, auto
import datetime
from config import Configuration
from lane import laneClient, laneBotClient
from lane.mongo.logging_mongo import is_logging_enabled, set_logging
from pyrogram import filters
from pyrogram.types import Message

LOGGING_ON = ['on', 'yes', '1', 'true']
LOGGING_OFF = ['off', 'no', '0', 'false']

@laneClient.on_message(filters.command('logger', '.') & filters.me)
async def log(lane, message):
    toggle = message.command[1]
    if toggle in LOGGING_ON:
        set_logging(toggle=True)
        await message.edit("`Enabled logger.`")
    elif toggle in LOGGING_OFF:
        set_logging(toggle=False)
        await message.edit("`Disabled logger.`")

@laneClient.on_message(filters.private)
async def forward(lane, message):
    if is_logging_enabled():
        await forward_as_copy(message)
        # await laneBotClient.forward_messages(
        #     chat_id=Configuration.PM_LOGGER_ID,
        #     from_chat_id=message.chat.id,
        #     message_ids=message.message_id
        # )
         
class messageType(Enum):
    text = auto()
    sticker = auto()
    animation= auto()
    document = auto()
    photo = auto()
    audio = auto()
    voice = auto()
    video = auto()
    video_note = auto()

def getMessage(message: Message):
    data_type = 0
    content = None
    text = None
    
    from_user = f'{message.from_user.mention} - (`{message.from_user.id}`)'
    from_chat = f'@{message.chat.username} - (`{message.chat.id}`)'
    time = message.date
    converted_time = datetime.datetime.fromtimestamp(time)

    if message.text:
        data_type = messageType.text.value 
        text = message.text.markdown
    elif message.sticker:
        data_type = messageType.sticker.value
        content = message.sticker.file_id 
    elif message.animation:
        data_type = messageType.animation.value
        content = message.animation.file_id
    elif message.document:
        data_type = messageType.document.value
        content = message.document.file_id
        if message.caption:
            text = message.caption.markdown
    elif message.photo:
        data_type = messageType.photo.value
        content = message.photo.file_id
        if message.caption:
            text = message.caption.markdown
    elif message.audio:
        data_type = messageType.audio.value
        content = message.audio.file_id
        if message.caption:
            text = message.caption.markdown
    elif message.voice:
        data_type = messageType.voice.value
        content = message.voice.file_id
        if message.caption:
            text = message.caption.markdown
    elif message.video:
        data_type = messageType.video.value
        content = message.video.file_id
        if message.caption:
            text = message.caption.markdown
    elif message.video_note:
        data_type = messageType.video_note.value
        content = message.video_note.file_id
    
    return (
        data_type,
        content,
        text,
        converted_time,
        from_user,
        from_chat
    )


async def forward_as_copy(message: Message):
    data_type, content, text, converted_time, from_user, from_chat = getMessage(message=message)
    if text:
        text = (
            f'**Text:** `{text}`\n\n'
            f'**From Chat:** {from_chat}\n'
            f'**From User:** {from_user}\n'
            f'**Date:** `{converted_time}`\n'
        )
        
    else:
        text = (
            f'**From Chat:** {from_chat}\n'
            f'**From User:** {from_user}\n'
            f'**Date:** `{converted_time}`\n'
        )

    if data_type == 1:
        await laneBotClient.send_message(
            chat_id=Configuration.PM_LOGGER_ID,
            text=text
        )
    elif data_type == 2:
        log = await laneBotClient.send_sticker(
            chat_id=Configuration.PM_LOGGER_ID,
            sticker=content
        )
        await log.reply(
            text=text
        )

    elif data_type == 3:
        log = await laneClient.send_animation(
            chat_id=Configuration.PM_LOGGER_ID,
            animation=content
        )
        await log.reply(
            text=text
        )

    elif data_type == 4:
        await laneClient.send_document(
            chat_id=Configuration.PM_LOGGER_ID,
            document=content,
            caption=text
        )

    elif data_type == 5:
        await laneClient.send_photo(
            chat_id=Configuration.PM_LOGGER_ID,
            photo=f"{message.photo.file_id} {message.photo.file_unique_id}",
            caption=text
        )
        
    elif data_type == 6:
        await laneClient.send_audio(
            chat_id=Configuration.PM_LOGGER_ID,
            audio=content,
            caption=text
        )
    elif data_type == 7:
        await laneClient.send_voice(
            chat_id=Configuration.PM_LOGGER_ID,
            voice=content,
            caption=text
        )
    elif data_type == 8:
        await laneClient.send_video(
            chat_id=Configuration.PM_LOGGER_ID,
            video=content,
            caption=text
        )
    elif data_type == 9:
        log = await laneClient.send_video_note(
            chat_id=Configuration.PM_LOGGER_ID,
            video_note=content
        )
        await log.reply(
            text=text
        )
            
 