from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/27d19ab9fcc9f7d6baa24.jpg",
    "https://telegra.ph/file/352f774670535d133a152.jpg",
    "https://telegra.ph/file/c47c2460f30c3d45bfda9.jpg",
    "https://telegra.ph/file/d073798b5f1d8f4b8ab06.jpg",
    "https://telegra.ph/file/60f9b3b350a8fd2d742ba.jpg",
    "https://telegra.ph/file/f66c6e609c0c4933f7c15.jpg",
    "https://telegra.ph/file/38be78f0c602d573b24ea.jpg",
]

HEY_IMG = "https://telegra.ph/file/27d19ab9fcc9f7d6baa24.jpg"

ALIVE_ANIMATION = [
    "https://graph.org/file/88588f0bc3aa006b7a3fb.mp4",
    "https://graph.org/file/88588f0bc3aa006b7a3fb.mp4",
    "https://graph.org/file/88588f0bc3aa006b7a3fb.mp4",
    "https://graph.org/file/88588f0bc3aa006b7a3fb.mp4",
]

FIRST_PART_TEXT = "⚡️ *ʜᴇʟʟᴏ* {} . . ."

PM_START_TEXT = "⚡️ *ɪ ᴀᴍ ushio, ᴀ Summer time rendering ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⛩ 𝙍𝙚𝙘𝙧𝙪𝙞𝙩 𝙈𝙚 ⛩",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", url=f"https://t.me/naruto_support1"),
    ],
   [
        InlineKeyboardButton(text="my master⚡️", url=f"https://t.me/naruto_of_telegram"),
    ],
    
    [
        InlineKeyboardButton(text="𝙨𝙠𝙞𝙡𝙡𝙨 ⚔️", callback_data="help_back"),
        InlineKeyboardButton(text="🖥️𝗜𝗡𝗦𝗜𝗗𝗘𝗥", callback_data="insider_"),
    ],
    [
        InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥🌚", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⛩ 𝙍𝙚𝙘𝙧𝙪𝙞𝙩 𝙈𝙚 ⛩",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥🌚", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(
            text="⛩ 𝙍𝙚𝙘𝙧𝙪𝙞𝙩 𝙈𝙚 ⛩",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
        ib(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", url="https://t.me/naruto_support1"),
    ],
]

HELP_STRINGS = """
*𝗨𝗦𝗛𝗜𝗢-𝗞𝗢𝗙𝗨𝗡* 

*Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
