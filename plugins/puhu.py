from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


async def afisgetir(bot, message):
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


@Client.on_message(filters.command('a101'))
async def a101getir(bot, message):
    try:
       afisler = await afisgetir(bot, message)
       for photo in afisler:
           await message.reply_photo(photo)
    except Exception as e:
        await message.reply_text(e)
