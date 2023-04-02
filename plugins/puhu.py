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

async def aldinaldingelecekhafta(bot, message):
    try:
        url = "https://www.a101.com.tr/aldin-aldin-gelecek-hafta-brosuru"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        return fotolar
    except Exception as e:
        await message.reply_text(e)

async def aldinaldinbuhafta(bot, message):
    try:
        url = "https://www.a101.com.tr/aldin-aldin-bu-hafta-brosuru"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        return fotolar
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('a101'))
async def a101getir(bot, message):
    try:
       text = "Merhaba {message.from_user.mention},\nAşağıdaki butoblardan hangi afişleri istediğiniz seç 😊"
       buton = [[
           InlineKeyboardButton(f'A101 Bu Hafta Aldın Aldın', callback_data='buhaftaaldin'),
           InlineKeyboardButton(f'A101 Gelecek Hafta Aldın Aldın', callback_data='gelecekhaftaaldin')
           ],[
           InlineKeyboardButton(f'A101 Bu Haftanın Yıldızları', callback_data='buhaftayildiz'),
           InlineKeyboardButton(f'A101 Gelecek Haftanın Yıldızları', callback_data="gelecekhaftayildiz")
           ]]
       butonlar = InlineKeyboardMarkup(buton)
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)
