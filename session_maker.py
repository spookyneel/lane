import pyrogram
from pyrogram import Client


api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with Client("lane", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> <code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")