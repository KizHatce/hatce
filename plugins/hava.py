from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
import math
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command('hava'))
async def havabilgisi(bot, message):
    try:
        mes = message.text.split(" ")
        if len(mes) == 3:
            il = mes[1]
            ilce = mes[2]
        elif len(mes) == 2:
            il = mes[1]
            ilce = mes[1]
        elif len(mes) == 1:
            await message.reply_text("Hatalı Kullanım Şunu dene:\n\n`/hava İstanbul Avcılar`")
            return
        url = f"https://www.google.com/search?&q={il}+{ilce}+hava+durumu&lr=lang_tr&hl=tr"
        istek = requests.get(url)
        corba = BeautifulSoup(istek.content, "lxml")
        bilgi = corba.findAll('div', class_='BNeawe')
        gun, durum = bilgi[3].text.strip().split('\n')
        derece_temp = corba.find('div', class_='BNeawe').text.split("°F")
        dereceint = int(derece_temp[0])
        derecetemp = dereceint - 32
        derece = derecetemp / 5/9
        LOGGER.info(corba)
        await message.reply_text(f"{il}/{ilce} Hava Durumu:\n\nGün: {gun}\nDurum: {durum}\nDerece: {derece}°C")
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('foto'))
async def fotogetir(bot, message):
    try:
        aranacaktemp = message.text.split(" ", 1)[1]
        aranacak = aranacaktemp.replace(" ", "+")
        url = f"https://www.google.com/search?q={aranacak}+&prmd=imnv&sxsrf=APwXEde70utXdHW4TzxSkD4soDMpiDzMag:1680124608010&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiB-sDzh4L-AhXDcvEDHU7WBE4Q_AUIHigB&biw=360&bih=662&dpr=3"
        istek = requests.get(url)
        corba = BeautifulSoup(istek.content, "lxml")
        fotourl = corba.findAll('div', class_='NZWO1b')
        for foto in fotourl:
            text1 = foto.find("img")
            text = text1.get("src")
            await message.reply_text(text)
        LOGGER.info(corba)
    except Exception as e:
        await message.reply_text(e)
