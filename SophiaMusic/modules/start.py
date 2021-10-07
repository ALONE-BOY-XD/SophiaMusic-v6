from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> Hi there,👋 {message.from_user.first_name}!
\nThis is 𝐊𝐈𝐋𝐋𝐄𝐑 𝐐𝐔𝐄𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓.
I play music on Telegram's Voice Chats.
\nFo More Help Use Buttons Below:
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐊𝐈𝐋𝐋𝐄𝐑 𝐐𝐔𝐄𝐄𝐍", url="https://t.me/killer_queen_x_d")
                  ],[
                    InlineKeyboardButton(
                        "𝐊𝐈𝐋𝐋𝐄𝐑 𝐊𝐈𝐍𝐆", url="https://t.me/dihanofficial"
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐇𝐀𝐓𝐓𝐈𝐍𝐆 𝐆𝐑𝐎𝐔𝐏", url="https://t.me/blinking_stars_op"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url="https://t.me/KILLER_QUEEN_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""*★彡[ᴋɪʟʟᴇʀ Qᴜᴇᴇɴ'ꜱ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪꜱ ᴀʟɪᴠᴇ]彡★.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘ", url="https://t.me/blinking_stars_op")
                ]
            ]
        )
   )


