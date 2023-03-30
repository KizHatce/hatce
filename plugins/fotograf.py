from pyrogram import Client, filters
import random
from pyromod import listen
import os

yaslar = ["57", "34", "52"]

async def dongu(bot, message, yas, say, tahmin):
    say +=1
    try:
        tah = int(tahmin)
    except:
        tedilen = await bot.ask(message.chat.id, "Lütfen Sayı Gir..")
        tahmin = tedilen.text
        await dongu(bot, message, yas, say, tahmin)
    if int(tahmin) > int(yas):
        tedilen = await bot.ask(message.chat.id, "Yanlış Cevap!\nAşağı İn.. ")
    elif int(tahmin) < int(yas):
        tedilen = await bot.ask(message.chat.id, "Yanlış Cevap!\nYukarı Çık.. ")
    elif int(tedilen.text) == int(yas):
        await message.reply_text(f"Tebrikler {say} deneyişte doğru cevabı buldun..")
    else:
        tahmin = tedilen.text
        await dongu(bot, message, yas, say, tahmin)

async def yastahmin(bot, message, yas, say):
    tedilen = await bot.ask(message.chat.id, "Yaşımı Bul Bakalım..")
    say +=1
    tahmin = tedilen.text
    try:
        tah = int(tahmin)
    except:
        tedilen = await bot.ask(message.chat.id, "Lütfen Sayı Gir..")
        tahmin = tedilen.text
        await dongu(bot, message, yas, say, tahmin)
    if int(tedilen.text) == int(yas):
        await message.reply_text(f"Tebrikler **{say}** deneyişte doğru cevabı buldun..")
    else:
        await dongu(bot, message, yas, say, tahmin)

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
        say = 0
        await yastahmin(bot, message, yas, say)
    except Exception as e:
        await message.reply_text(e)
   
