import asyncio
from modules.config import ALIVE_IMG
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""⍟━━━━━━━━━━━━━━━━━━━━━━━⍟
♫︎ ʟᴜᴄɪғᴇʀ ᴍᴜsɪᴄ ♫︎
✪ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ ᴅᴇᴠɪʟ ✪
 
┏━━━━━━━━━━━━━━━━━━━━━━┓
┣♡︎ ᴏᴜʀ ɢʀᴏᴜᴘ : [✯𝗟𝗨𝗫𝗖𝗟𝗨𝗕✯](https://t.me/luxclub_sergio)
┣♡︎ sᴜᴘᴘᴏʀᴛ : [✯𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣✯](https://t.me/luciferdevilshell)
┗━━━━━━━━━━━━━━━━━━━━━━┛

♫︎ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ?
ᴅᴍ ᴍʏ [ᴍᴀsᴛᴇʀ](https://t.me/LUCYY_xZz) ...
⍟━━━━━━━━━━━━━━━━━━━━━━━⍟""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ❰ ✪ ᴀʟsᴏ ᴊᴏɪɴ ✪ ❱ ", url=f"https://t.me/LUXCLUB_SERGIO")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "lucifermusic"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♡︎ 𝐖𝐚𝐲 𝐓𝐨 𝐋𝐔𝐗𝐂𝐋𝐔𝐁 ♡︎", url=f"https://t.me/LUXCLUB_SERGIO")
                ]
            ]
        ),
    )


