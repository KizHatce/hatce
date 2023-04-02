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
butonlar = InlineKeyboardMarkup([
           [InlineKeyboardButton(f'Bim Gelecek Hafta Salı', callback_data='bimges')],
           [InlineKeyboardButton(f'Bim Gelecek Hafta Cuma', callback_data='bimgec')],
           [InlineKeyboardButton(f'Bim Bu Hafta Salı', callback_data='bimbs')],
           [InlineKeyboardButton(f'Bim Bu Hafta Cuma', callback_data='bimbc')],
           [InlineKeyboardButton(f'Bim Geçen Hafta Salı', callback_data='bimgs')],
           [InlineKeyboardButton(f'Bim Geçen Hafta Cuma', callback_data='bimgc')]])

async def bimgecenhaftasali(bot, message):
    try:
        fotolar = []
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
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


async def bimgecenhaftacuma(bot, message):
    try:
        fotolar = []
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        filtre = c.findAll('a', attrs={"class":"download"})
        sec = filtre[1]
        href = sec.get('href')
        foto = f"https://www.bim.com.tr{href}"
        fotolar.append(foto)
        kucukler = c.findAll('div', attrs={"class":"smallArea col-4 col-md-3"})[1] 
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
            text = "Bim Geçen Hafta Cuma Broşürleri Getirildi..") 
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  

async def bimbuhaftasali(bot, message):
    try:
        fotolar = []
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        filtre = c.findAll('a', attrs={"class":"download"})
        sec = filtre[2]
        href = sec.get('href')
        foto = f"https://www.bim.com.tr{href}"
        fotolar.append(foto)
        kucukler = c.findAll('div', attrs={"class":"smallArea col-4 col-md-3"})[2] 
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
            text = "Bim Bu Hafta Salı Broşürleri Getirildi..")    
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  


async def bimbuhaftacuma(bot, message):
    try:
        fotolar = []
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        filtre = c.findAll('a', attrs={"class":"download"})
        sec = filtre[3]
        href = sec.get('href')
        foto = f"https://www.bim.com.tr{href}"
        fotolar.append(foto)
        kucukler = c.findAll('div', attrs={"class":"smallArea col-4 col-md-3"})[3] 
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
            text = "Bim Bu Hafta Cuma Broşürleri Getirildi..")
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  

async def bimgelecekhaftasali(bot, message):
    try:
        fotolar = []
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        filtre = c.findAll('a', attrs={"class":"download"})
        sec = filtre[4]
        href = sec.get('href')
        foto = f"https://www.bim.com.tr{href}"
        fotolar.append(foto)
        kucukler = c.findAll('div', attrs={"class":"smallArea col-4 col-md-3"})[4] 
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
            text = "Bim Gelecek Hafta Salı Broşürleri Getirildi..")    
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  


async def bimgelecekhaftacuma(bot, message):
    try:
        fotolar = []
        url = "https://www.bim.com.tr/Categories/680/afisler.aspx"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        filtre = c.findAll('a', attrs={"class":"download"})
        sec = filtre[5]
        href = sec.get('href')
        foto = f"https://www.bim.com.tr{href}"
        fotolar.append(foto)
        kucukler = c.findAll('div', attrs={"class":"smallArea col-4 col-md-3"})[5] 
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
            text = "Bim Gelecek Hafta Cuma Broşürleri Getirildi..")
    except Exception as e:
       await bot.send_message(
            chat_id = message.from_user.id,
            text = e)  

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

@Client.on_callback_query(filters.regex('^bimgs$'))
async def bimsaligetir(bot, message):
    await message.answer("Geçen Hafta'ki Bim Salı Broşürü Getiriliyor...",
                         show_alert=True)
    await bimgecenhaftasali(bot, message)

@Client.on_callback_query(filters.regex('^bimgc$'))
async def bimcumagetir(bot, message):
    await message.answer("Geçen Hafta'ki Bim Cuma Broşürü Getiriliyor...",
                         show_alert=True)
    await bimgecenhaftacuma(bot, message)

@Client.on_callback_query(filters.regex('^bimbs$'))
async def bimbusaligetir(bot, message):
    await message.answer("Bu Hafta'ki Bim Salı Broşürü Getiriliyor...",
                         show_alert=True)
    await bimbuhaftasali(bot, message)

@Client.on_callback_query(filters.regex('^bimbc$'))
async def bimbucumagetir(bot, message):
    await message.answer("Bu Hafta'ki Bim Cuma Broşürü Getiriliyor...",
                         show_alert=True)
    await bimbuhaftacuma(bot, message)

@Client.on_callback_query(filters.regex('^bimges$'))
async def bimgeleceksaligetir(bot, message):
    await message.answer("Gelecek Hafta'ki Bim Salı Broşürü Getiriliyor...",
                         show_alert=True)
    await bimgelecekhaftasali(bot, message)

@Client.on_callback_query(filters.regex('^bimgec$'))
async def bimgelecekcumagetir(bot, message):
    await message.answer("Gelecek Hafta'ki Bim Cuma Broşürü Getiriliyor...",
                         show_alert=True)
    await bimgelecekhaftacuma(bot, message)
