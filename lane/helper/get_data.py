from lane import laneClient
from pyrogram.types import Message

async def admin_check(message: Message) -> bool:
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await laneClient.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ['creator', 'administrator']
    return check_status.status in admin_strings

def get_reason(message):
    if( 
        message.reply_to_message
    ):
        if (
            len(message.command) >= 2
            and (
                message.command[1].startswith('@')
                or (
                        message.command[1].isdigit()
                        and (
                            len(message.command[1]) >= 5
                            or len(message.command[1]) <=15
                        )
                )
            )
        ):
            text = ' '.join(message.command[2:])
        else:
            text = ' '.join(message.command[1:])
    
    elif (
        not message.reply_to_message
    ):
        text = ' '.join(message.command[2:])
    
    return text

def get_text(message):
    if( 
        message.reply_to_message
    ):
        if (
            len(message.command) >= 2
            and (
                message.command[1].startswith('@')
                or (
                        message.command[1].isdigit()
                        and (
                            len(message.command[1]) >= 5
                            or len(message.command[1]) <=15
                        )
                )
            )
        ):
            text = ' '.join(message.command[2:])
        else:
            text = ' '.join(message.command[1:])
    
    elif (
        not message.reply_to_message
    ):
        text = ' '.join(message.command[2:])
    
    return text    