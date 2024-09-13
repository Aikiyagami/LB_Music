from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘼𝙙𝙙 𝙈𝙚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="𝙃𝙚𝙡𝙥 & 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨", callback_data="settings_back_helper"),
        ],
    ]
    return buttons
