from pyrogram import Client, filters
import random
from pyromod import listen
import os

@Client.on_message(filters.command('foto'))
async def fotooyunu(bot, message):
    try:
        dosya = random.randint(0, 3)
        dir = "plugins/fotolar"
        temp = os.listdir(dir)[dosya]
        photo = f"plugins/fotolar/{temp}"
        await message.reply_photo(photo)
    except Exception as e:
        await message.reply_text(e)
   
