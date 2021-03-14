from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am hermione 💚 Music Player🎶 that lets you play music in your Telegram groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "follow me instragram❤", url="https://www.instagram.com/mr.matheesha_official?r=nametag"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/sibertrone_tf"
                    ),
                    InlineKeyboardButton(
                        "owner", url="https://t.me/percy_jackson_4"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
