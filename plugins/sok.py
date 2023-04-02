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
           [InlineKeyboardButton(f'Şok Haftasonu Fırsatları', callback_data='sokhsy')]])

carsamba = "https://kurumsal.sokmarket.com.tr/firsatlar/carsamba"
haftasonu = "https://kurumsal.sokmarket.com.tr/firsatlar/hafta-sonu"

@Client.on_message(filters.command('sok') & filters.private)
async def sokgetir(bot, message):
    try:
       text = f"Merhaba {message.from_user.mention},\nAşağıdaki butonlardan hangi Broşürleri istediğini seç 😊"
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)

@Client.on_callback_query(filters.regex('^sokhy$'))
async def sokhaftaici(bot, message):
    await message.answer("Şok Haftanın Fırsatları Broşürü Getiriliyor...",
                         show_alert=True)
    try:
        istek = requests.get(carsamba)
        dosyam = "Şok Haftanın Fırsatları.pdf"
        with open(dosyam, "wb") as dosya:
               dosya.write(istek.content)
        await bot.send_document(
            chat_id = message.from_user.id, 
            caption = "Şok Haftanın Fırsatları",
            document = dosyam) 
    except Exception as e:
        LOGGER.info(e)

@Client.on_callback_query(filters.regex('^sokhsy$'))
async def sokhaftasonu(bot, message):
    await message.answer("Şok Haftanın Fırsatları Broşürü Getiriliyor...",
                         show_alert=True)
    try:
        istek = requests.get(haftasonu)
        dosyam = "Şok Haftasonu Fırsatları.pdf"
        with open(dosyam, "wb") as dosya:
               dosya.write(istek.content)
        await bot.send_document(
            chat_id = message.from_user.id, 
            caption = "Şok Haftasonu Fırsatları",
            document = dosyam) 
    except Exception as e:
        LOGGER.info(e)
