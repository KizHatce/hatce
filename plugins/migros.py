# Coded by @mmagneto (:d) 

from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
from pdf2image import convert_from_path
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
butonlar = InlineKeyboardMarkup([[
           InlineKeyboardButton(f'Migros Bu Hafta', callback_data='migrosg')],
           [InlineKeyboardButton(f'Migros Geçen Hafta', callback_data='migrosgecenn')]])

async def migrosgecen(bot, message):
    try:
        url = "https://www.money.com.tr/migroskop-dijital"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        brosurler = c.findAll('a', attrs={"class":"_df_button"})[0]
        uri = brosurler.get("source")
        tarih = brosurler.get("mcdate")
        istek = requests.get(uri)
        file = uri.split("mcstage/")
        file_name = file[1]
        with open(file_name, "wb") as dosya:
            dosya.write(istek.content) 
        await bot.send_document(
            chat_id = message.from_user.id,
            document = file_name,
            caption = tarih)
        images = convert_from_path(file_name)
        for img in images:
            await bot.send_photo(
                chat_id = message.from_user.id, 
                photo = img)
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

async def migrosguncel(bot, message):
    try:
        url = "https://www.money.com.tr/migroskop-dijital"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        brosurler = c.findAll('button', attrs={"class":"btn btn-white-purple-line center-block _df_button"})[0]
        tarih = brosurler.get("mcdate")
        uri = brosurler.get("source")
        istek = requests.get(uri)
        file = uri.split("mcstage/")
        file_name = file[1]
        with open(file_name, "wb") as dosya:
            dosya.write(istek.content) 
        await bot.send_document(
            chat_id = message.from_user.id,
            document = file_name,
            caption = tarih)
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

@Client.on_callback_query(filters.regex('^migrosgecenn$'))
async def migrosgecengetir(bot, message):
    await message.answer("Geçen Haftaki Migros Broşürü Getiriliyor...",
                         show_alert=True)
    await migrosgecen(bot, message)
