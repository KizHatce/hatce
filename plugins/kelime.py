from pyrogram import Client, filters
from pyromod import listen
import random

async def dongu(bot, message, sayi, say):
    say +=1
    tedilen = await bot.ask(message.from_user.id, "Yanlış Cevap!")
    if int(tedilen.text) == sayi:
        await message.reply_text(f"Tebrikler {say} deneyişte doğru cevabı buldun..")
    else:
        await dongu(bot, message, sayi, say)

async def sayitahmin(bot, message, sayi, say):
    tedilen = await bot.ask(message.from_user.id, "aklımdan bir sayı tuttum bul bakalım..")
    say +=1
    if int(tedilen.text) == sayi:
        await message.reply_text(f"Tebrikler {say} deneyişte doğru cevabı buldun..")
    else:
        await dongu(bot, message, sayi, say)

@Client.on_message(filters.command('sayi'))
async def sayioyunu(bot, message):
    try:
        sayi = random.randint(1, 10) # 1 ile 1000 arasından bir sayı seçtiriyorum.
        say = 0
        await sayitahmin(bot, message, sayi, say)
    except Exception as e:
        await message.reply_text(e)
