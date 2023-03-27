# CODED BY :d

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command('start'))
async def start(bot, message):
    name = message.from_user.first_name
    url = "https://t.me/mmagneto"
    text = f"Merhaba {name}\n\nBu bot sayesinde yașadığın yerdeki iftar ve sahur saatlerini ve ne kadar kaldığını öğrenebilirsin 😁.\n\n`/sahur İstanbul Avcılar`\n`/iftar İstanbul Avcılar`\n\nHayırlı Ramazanlar [:d]({url})"
    photo = "https://telegra.ph/file/f3cb49e5aa241bc8a2a8a.jpg"
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo, 
        caption=text, 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Beni Oluşturan", url="https://t.me/mmagneto")]]))
        
