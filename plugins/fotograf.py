from pyrogram import Client, filters
import random
from pyromod import listen
import os

yaslar = ["57", "34", "55", "52"]

@Client.on_message(filters.command('foto'))
async def fotooyunu(bot, message):
    try:
        dosya = random.randint(0, 3)
        dir = "plugins/fotolar1"
        temp = os.listdir(dir)[dosya]
        photo = f"plugins/fotolar1/{temp}"
        yas = yaslar[dosya]
        await message.reply_photo(
            photo=photo,
            caption="Hadi Bakalım Yaşımı Tahmin Et! 👌")
    except Exception as e:
        await message.reply_text(e)
   
