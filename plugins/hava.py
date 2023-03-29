from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
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
        derece = corba.find('div', class_='BNeawe').text
        LOGGER.info(corba)
        await message.reply_text(f"{il}/{ilce} Hava Durumu:\n\nGün: {gun}\nDurum: {durum}\nDerece: {derece}")
    except Exception as e:
        await message.reply_text(e)
