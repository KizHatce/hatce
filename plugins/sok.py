from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
butonlar = InlineKeyboardMarkup([
           [InlineKeyboardButton(f'Şok Haftanın Fırsatları', callback_data='sokhy')],
           [InlineKeyboardButton(f'Şok Haftasonu Fırsatları', callback_data='bimgec')]])

async def sokhaftaninyildizi(bot, message):
    try:
        fotolar = []
        url = "https://kurumsal.sokmarket.com.tr/haftanin-firsatlari/firsatlar"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        LOGGER.info(c)
        filtre = c.findAll('a', attrs={"class":"download"})
        sec = filtre[0]
        href = sec.get('href')
        foto = f"https://www.bim.com.tr{href}"
        fotolar.append(foto)
        kucukler = c.findAll('div', attrs={"class":"smallArea col-4 col-md-3"})[0] 
        smal = kucukler.findAll('a', attrs={"class":"small"})
        for i in smal:
            href = i.get("data-bigimg")
            foto =  f"https://www.bim.com.tr{href}"
            fotolar.append(foto)
        for foto in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = foto)
        await bot.send_message(
            chat_id = message.from_user.id,
            text = "Bim Geçen Hafta Salı Broşürleri Getirildi..")   
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  

@Client.on_message(filters.command('sok') & filters.private)
async def bimgetir(bot, message):
    try:
       text = f"Merhaba {message.from_user.mention},\nAşağıdaki butonlardan hangi Broşürleri istediğini seç 😊"
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)

@Client.on_callback_query(filters.regex('^sokhy$'))
async def bimsaligetir(bot, message):
    await message.answer("Şok Haftanın Yıldızları Broşürü Getiriliyor...",
                         show_alert=True)
    await sokhaftaninyildizi(bot, message)
