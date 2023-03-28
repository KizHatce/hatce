from pyrogram import Client, filters
from pyromod import listen
import random

async def dongu(bot, message, sayi, say, tahmin):
    say +=1
    if int(tahmin) > sayi:
        tedilen = await bot.ask(message.chat.id, "Yanlış Cevap!\nAşağı İn.. ")
    elif int(tahmin) < sayi:
        tedilen = await bot.ask(message.chat.id, "Yanlış Cevap!\nYukarı Çık.. ")
    if int(tedilen.text) == sayi:
        await message.reply_text(f"Tebrikler {say} deneyişte doğru cevabı buldun..")
    else:
        await dongu(bot, message, sayi, say)

async def sayitahmin(bot, message, sayi, say):
    tedilen = await bot.ask(message.chat.id, "aklımdan bir sayı tuttum bul bakalım..")
    say +=1
    tahmin = tedilen.text
    if int(tedilen.text) == sayi:
        await message.reply_text(f"Tebrikler **{say}** deneyişte doğru cevabı buldun..")
    else:
        await dongu(bot, message, sayi, say, tahmin)

@Client.on_message(filters.command('sayi'))
async def sayioyunu(bot, message):
    try:
        sayi = random.randint(1, 100) # 1 ile 1000 arasından bir sayı seçtiriyorum.
        say = 0
        await sayitahmin(bot, message, sayi, say)
    except Exception as e:
        await message.reply_text(e)
