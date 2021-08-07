import asyncio
from getpass import getuser
from os import geteuid, remove

from lane import laneClient
from pyrogram import filters


@laneClient.on_message(filters.command('exec', '.') & filters.me)
async def exec(lane, message):
  
  curruser = message.from_user.first_name
  try:
    uid = geteuid()
  except ImportError:
    uid = "This ain't it chief!"
  
  if not len(message.command) >= 2:
    await message.edit('give a command!')
    return
  
  command = message.text[len(message.command[0]) + 2:]
  print(command)
  process = await asyncio.create_subprocess_shell(
    command,
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE
    )
  stdout, stderr = await process.communicate()
  result = str(stdout.decode().strip()) + str(stderr.decode().strip())
  
  # If result length is greater than 4096 send result as .txt file
  if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await laneClient.send_document(
          chat_id=message.chat.id,
          document='output.txt'
          )
        remove("output.txt")
        return

  if uid == 0:
    await message.edit(
      f"`{curruser}`  # `{command}`"
      f"\n\n`{result}`"
      )
      
  else:
    await message.edit(
      f"`{curruser}` $ `{command}`" 
      f"\n\n`{result}`"
      )