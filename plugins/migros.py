# Coded by @mmagneto (:d) 

from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
butonlar = InlineKeyboardMarkup([[
           InlineKeyboardButton(f'Migros Güncel', callback_data='migrosg')]])

async def migrosguncel(bot, message):
    try:
        url = "https://www.money.com.tr/migroskop-dijital"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        brosurler = c.findAll('a' attrs={"class":"_df_button"})[0]
        uri = brosurler.get("source")
        tarih = brosurler.get("mcdate")
        await bot.send_message(message.from_user.id, uri)
        istek = requests.get(uri)
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

@Client.on_message(filters.command('migros') & filters.private)
async def migros(bot, message):
    try:
       text = f"Merhaba {message.from_user.mention},\nAşağıdaki butonlardan hangi Broşürleri istediğini seç 😊"
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)

@Client.on_callback_query(filters.regex('^migrosg$'))
async def migrosguncelgetir(bot, message):
    await message.answer("Bu Hafta'ki Migros Broşürü Getiriliyor...",
                         show_alert=True)
    await migrosguncel(bot, message)
