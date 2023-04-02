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
           InlineKeyboardButton(f'A101 Bu Hafta Aldın Aldın', callback_data='buhaftaaldin')],
           [InlineKeyboardButton(f'A101 Gelecek Hafta Aldın Aldın', callback_data='gelecekhaftaaldin')
           ],[
           InlineKeyboardButton(f'A101 Haftanın Yıldızları', callback_data='haftayildiz')],
           [InlineKeyboardButton(f'A101 Hadi Fırsatları', callback_data="hadi")
           ],[
           InlineKeyboardButton(f'A101 Genel Kampanya', callback_data="a101genel")
           ]]) 

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
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "Aldın Aldın Gelecek Hafta Broşürleri Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

async def haftaninyildizlari(bot, message):
    try:
        url = "https://www.a101.com.tr/afisler-haftanin-yildizlari"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "Haftanın Yıldızları Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

async def a101genel(bot, message):
    try:
        url = "https://www.a101.com.tr/buyuk-oldugu-icin-ucuz-afisler"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "A101 Genel Kampanyaları Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e) 

async def a101hadi(bot, message):
    try:
        url = "https://www.a101.com.tr/afisler-hadi"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "A101 Hadi Fırsatları Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

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
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "Aldın Aldın Bu Hafta Broşürleri Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

@Client.on_message(filters.command('a101') & filters.private)
async def a101getir(bot, message):
    try:
       text = f"Merhaba {message.from_user.mention},\nAşağıdaki butonlardan hangi Broşürleri istediğini seç 😊"
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)

@Client.on_callback_query(filters.regex('^buhaftaaldin$'))
async def aldinaldinbugetir(bot, message):
    await message.answer("Bu Hafta Aldın Aldın Broşürleri Getiriliyor...",
                         show_alert=True)
    await aldinaldinbuhafta(bot, message)

@Client.on_callback_query(filters.regex('^gelecekhaftaaldin$'))
async def aldinaldingelecekgetir(bot, message):
    await message.answer("Gelecek Hafta Aldın Aldın Broşürleri Getiriliyor...",
                         show_alert=True)
    await aldinaldingelecekhafta(bot, message)

@Client.on_callback_query(filters.regex('^haftayildiz$'))
async def haftaninyildizlarigetir(bot, message):
    await message.answer("Haftanın Yıldızları Getiriliyor...",
                         show_alert=True)
    await haftaninyildizlari(bot, message)

@Client.on_callback_query(filters.regex('^hadi$'))
async def a101hadigetir(bot, message):
    await message.answer("A101 Hadi Fırsatları Getiriliyor...",
                         show_alert=True)
    await a101hadi(bot, message)

@Client.on_callback_query(filters.regex('^a101genel$'))
async def a101genelgetir(bot, message):
    await message.answer("A101 Genel Kampanyalar Getiriliyor...",
                         show_alert=True)
    await a101genel(bot, message)
