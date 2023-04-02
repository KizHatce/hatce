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
           InlineKeyboardButton(f'Bim Bu Hafta Salı', callback_data='bimbs')],
           [InlineKeyboardButton(f'Bim Bu Hafta Cuma', callback_data='bimbc')]])

@Client.on_message(filters.command('bim') & filters.private)
async def bimgetir(bot, message):
    try:
       text = f"Merhaba {message.from_user.mention},\nAşağıdaki butonlardan hangi Broşürleri istediğini seç 😊"
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)

@Client.on_callback_query(filters.regex('^bimbs$'))
async def bimsaligetir(bot, message):
    await message.answer("Bu Hafta'ki Bim Salı Broşürü Getiriliyor...",
                         show_alert=True)
    try:
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        filtre = c.findAll('a', attrs={"class":"download"})
        await bot.send_photo(
            chat_id = message.from_user.id,
            photo = foto) 
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  
