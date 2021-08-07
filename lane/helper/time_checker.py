from lane.helper.convert import convert_time

async def get_time(message):
    if(
        message.reply_to_message
    ):
        if not (
            len(message.command) >= 2
        ):
            await message.edit(
                "`Specify a time bozo`"
            )
            return None

        args = message.command[1]
        if await check_time(message, args):
            return args
        
    elif not (
        message.reply_to_message
    ):
        if not len(message.command) >= 3:
            await message.edit(
                "`Specify a time bozo`"
            )
            return None

        args = message.command[2]
        if await check_time(message, args):
            return args
            

async def check_time(message, args) -> bool:
    if len(args) == 0:
        await message.edit(
            f"`Provide time bozo`"
        )
        return False
        
    if (
        len(args) == 1
    ):
        await message.edit(
            (
                f"`Wtf is: '{args[-1]}' shit does not follow the expected time patterns`\n"
            )
        )
        return False

    elif len(args) > 1:
        if not args[-2].isdigit():
            await message.edit(
                f"`Wtf: '{args[-2]}' ain't a valid number bozo`"
            )
            return False

        elif args[-1] in ['w', 'd', 'h', 'm']:
            check_time_limit = convert_time(int(args[:-1]), args[-1])
            if check_time_limit >= 31622400: #  31622400 ( seconds ) is 366 days 
                await message.edit(
                    "`Nigga you forgotten how telegram works or sm?`"
                )
                return False
            return True
        else:
            await message.reply(
                    f"`Wtf is: '{args[-1]}' ain't a valid number bozo`"
                )
            return False

def time_string_helper(time_args):
    time_limit = int(time_args[:-1])
    if time_args[-1] == 'w':
        time_format = 'weeks'
    elif time_args[-1] == 'd':
        time_format = 'days'
    elif time_args[-1] == 'h':
        time_format = 'hours'
    elif time_args[-1] == 'm':
        time_format = 'mintues'
    return time_limit, time_format