from lane import laneClient

async def get_user(message):
    if(
        message.reply_to_message
        and not message.forward_from
    ):
        if (
            len(message.command) >= 2
        ):
            args = message.command[1]
            if (
                args.startswith('@')
                or (
                    args.isdigit()
                    and (
                        len(args) >= 5
                        or len(args) <=15
                    )
                )
            ):
                user_info = await laneClient.get_users(
                    user_ids=args
                )
                return user_info
            else:
                user_info = message.reply_to_message.from_user
                return user_info
        else:
            user_info = message.reply_to_message.from_user
            return user_info 

    elif (
        message.forward_from
    ):
        user_info = message.forward_from
        return user_info 

    elif not (
        message.reply_to_message
        or message.forward_from
    ):
        if not (
            len(message.command) >= 2
        ):
            await message.edit(
                "`Specify a user bozo`"
            )
            return False
            
        user = message.command[1]
        user_info = await laneClient.get_users(
            user_ids=user
        )
        
        return user_info