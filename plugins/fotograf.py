from pyrogram import Client, filters
import random
from pyromod import listen
import os

@Client.on_message(filters.command('foto'))
async def fotooyunu(bot, message):
    try:
        dosya = random.randint(1, 3)
        say = 1
        fotolar = "fotolar"
        for photo in os.listdir(fotolar):
            if int(say) == dosya:
                await message.reply_photo(photo)
            say +=1
    except Exception as e:
        await message.reply_text(e)
   
