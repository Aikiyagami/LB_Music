from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/9db70cb7ab32299aad914.jpg",
    "https://graph.org/file/0ce0901a95ec7cd5897df.jpg",
    "https://graph.org/file/88007011ac6e07b92aa92.jpg",
    "https://graph.org/file/77f3c9955282f900213de.jpg",
    "https://graph.org/file/9db70cb7ab32299aad914.jpg",
    "https://graph.org/file/9db70cb7ab32299aad914.jpg",
    "https://graph.org/file/0ce0901a95ec7cd5897df.jpg",
]

HEY_IMG = "https://graph.org/file/b0e39b61c92af66f6aaf8.jpg"

ALIVE_ANIMATION = [
    "https://graph.org/file/65030dc9f2c0d53c9621d.jpg",
    "https://graph.org/file/0fa70daf640d9dcf7c05a.jpg",
    "https://graph.org/file/b0e39b61c92af66f6aaf8.jpg",
    "https://graph.org/file/88007011ac6e07b92aa92.jpg",
]

FIRST_PART_TEXT = "⚡️ *ʜᴇʟʟᴏ* {} . . ."

PM_START_TEXT = "✨ ɪ ᴀᴍ 𝙷𝚞𝚝𝚊𝚘, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ"

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
        ib(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", url="https://t.me/beasts_community"),
    ],
]

HELP_STRINGS = """
*𝙷𝚞𝚝𝚊𝚘* 

*Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
