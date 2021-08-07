from lane import laneClient, anilist
from pyrogram import filters
import datetime


@laneClient.on_message(filters.command('anime', '.') & filters.me)
async def anime(lane, message):
    anime = message.command
    res = ""
    if len(anime) > 1:
        res = " ".join(anime[1:])
        await message.edit("`Fetching data...`")
    elif len(anime) == 1:
        await message.edit("`Who's gonna put deez args?`")

    r = await anilist.anime(res)
    print(r)
    banner = 'https://img.anili.st/media/{}'.format(r['id'])
    desc = shorten(r['description'])
    genre = r['genres']
    text = '**Romaji Title:** `{}`\n'.format(r['title']['romaji'])
    text += '**English Title:** `{}`\n'.format(r['title']['english'])
    text += '**Native Title:** `{}`\n'.format(r['title']['native'])
    text += '**Type:** `{} {}`\n\n'.format(r['type'], r['format'])
    text += '**Status:** `{}`\n'.format(r['status'])
    text += '**Runtime:** `{} minutes`\n\n'.format(r['duration'])
    text += '**Start year and season:** `{}` `{}`\n'.format(r['season'], r['startDate']['year'])
    text += '**Genres:** `{}`\n'.format(', '.join(genre))
    text += '**Rating:** `{}`\n'.format(r['averageScore'])
    text += '**Studio:** `{}`\n'.format(r['studios']['nodes'][0]['name'])
    if not r['trailer'] == None:
        text += '**Trailer:** http://www.youtube.com/watch?v={}\n\n'.format(r['trailer']['id'])
    else:
        text += '**Trailer:** `N/A`\n'   
    text += '**Description:** {}\n'.format(desc)

    try:
        await laneClient.send_photo(
        chat_id=message.chat.id,
        photo=banner,
        caption=text
    )
        await message.delete()
    except KeyError:
        await message.edit("`Rest in piss bozo, couldn't parse info.`")    

def shorten(description, info="https://anilist.co"):
    msg = ""
    if len(description) > 700:
        description = description[0:600] + "..."
        msg += f"{description}[Read More]({info})"
    else:
        msg += f"{description}"
    return msg

@laneClient.on_message(filters.command('character', '.') & filters.me)
async def character(lane, message):
    character = message.command
    res = ""
    if len(character) > 1:
        res = " ".join(character[1:])
        await message.edit("`Fetching data...`")
    elif len(character) == 1:
        await message.edit("`Who's gonna put deez args?`")

    r = await anilist.character(res)
    bday = monthCon(r['dateOfBirth']['month'])
    print(r)
    img = r['image']['large']
    desc = shorten(r['description'])
    text = '**First Name:** `{}`\n'.format(r['name']['first'])
    text += '**Last Name:** `{}`\n'.format(r['name']['last'])
    text += '**Full Name:** `{}`\n'.format(r['name']['full'])
    text += '**Native:** `{}`\n\n'.format(r['name']['native'])
    text += '**Gender:** `{}`\n'.format(r['gender'])
    text += '**Age:** `{}`\n'.format(r['age'])
    text += '**Birthday:** `{} {}`\n'.format(bday, r['dateOfBirth']['day'])
    if r['bloodType'] is not None:
        text += '**Blood Type:** `{}`\n\n'.format(r['bloodType'])
    else:
        text += '**Blood Type:** `{}`\n\n'.format('Not found')    
    text += '**Description:** {}\n'.format(desc)

    try:
        await laneClient.send_photo(
        chat_id=message.chat.id,
        photo=img,
        caption=text
    )
        await message.delete()
    except KeyError:
        await message.edit("`Rest in piss bozo, couldn't parse info.`")

def monthCon(month_int):
    datetimeObj = datetime.datetime.strptime(str(month_int), '%m')
    return datetimeObj.strftime('%B')

@laneClient.on_message(filters.command('manga', '.') & filters.me)
async def manga(lane, message):
    manga = message.command
    res = ""
    if len(manga) > 1:
        res = " ".join(manga[1:])
        await message.edit("`Fetching data...`")
    elif len(manga) == 1:
        await message.edit("`Who's gonna put deez args?`")

    r = await anilist.manga(res)
    print(r)
    banner = 'https://img.anili.st/media/{}'.format(r['id'])
    desc = shorten(r['description'])
    genre = r['genres']
    text = '**Romaji Title:** `{}`\n'.format(r['title']['romaji'])
    text += '**English Title:** `{}`\n'.format(r['title']['english'])
    text += '**Native Title:** `{}`\n\n'.format(r['title']['native'])
    text += '**Type:** `{}`\n\n'.format(r['type'])
    text += '**Status:** `{}`\n'.format(r['status'])
    text += '**Start year:** `{}`\n'.format(r['startDate']['year'])
    text += '**Genres:** `{}`\n'.format(', '.join(genre))
    text += '**Rating:** `{}`\n\n'.format(r['averageScore'])
    text += '**Description:** {}\n'.format(desc)

    try:
        await laneClient.send_photo(
        chat_id=message.chat.id,
        photo=banner,
        caption=text
    )
        await message.delete()
    except KeyError:
        await message.edit("`Rest in piss bozo, couldn't parse info.`")

@laneClient.on_message(filters.command('airing', '.') & filters.me)
async def manga(lane, message):
    airing = message.command
    res = ""
    if len(airing) > 1:
        res = " ".join(airing[1:])
        await message.edit("`Fetching data...`")
    elif len(manga) == 1:
        await message.edit("`Who's gonna put deez args?`")

    r = await anilist.airing(res)
    print(r)
    banner = 'https://img.anili.st/media/{}'.format(r['id'])
    if r['nextAiringEpisode'] is not None:
        airing_in = r['nextAiringEpisode']['timeUntilAiring'] * 1000
        conv_time = convert_time(airing_in)
        aired_eps = r['nextAiringEpisode']['episode']
        text = '**Romaji Title:** `{}`\n'.format(r['title']['romaji'])
        text += '**English Title:** `{}`\n'.format(r['title']['english'])
        text += '**Native Title:** `{}`\n\n'.format(r['title']['native'])
        text += '**Next episode airing in:** `{}`\n'.format(conv_time)
        text += '**Episodes streamed:** `{}`\n'.format(aired_eps)
    else:
        text = '**Romaji Title:** `{}`\n'.format(r['title']['romaji'])
        text += '**English Title:** `{}`\n'.format(r['title']['english'])
        text += '**Native Title:** `{}`\n\n'.format(r['title']['native'])
        text += '**Sttatus:** `FINISHED`\n'
        text += '**Total episodes:** `{}`\n'.format(r['episodes'])  
    try:
        await laneClient.send_photo(
        chat_id=message.chat.id,
        photo=banner,
        caption=text
        )
        await message.delete()
    except KeyError:
        await message.edit("`Rest in piss bozo, couldn't parse info.`")
    
def convert_time(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    msg = (
        ((str(days) + ' Days, ') if days else '')
        + ((str(hours) + ' Hours, ') if hours else '')
        + ((str(minutes) + ' Minutes, ') if minutes else '')
        + ((str(seconds) + ' Seconds, ') if seconds else '')
        + ((str(milliseconds) + ' ms, ') if milliseconds else '')
    )
    return msg[:-2]    
    


    


