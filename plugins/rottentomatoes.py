from pyrogram import Client, filters
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

session = requests.Session()

@Client.on_message(filters.command('rotten'))
async def rottent(bot, message):
    try:
        mes = message.text.split(" ", 1)
        url1 = mes[1]
        url2 = url1.replace(" ", "")
        url = f"https://www.rottentomatoes.com/search?search={url2}"
        istek = requests.get(url) 
        corba = BeautifulSoup(istek.content, "lxml")
        bilgi = corba.find('div', id='search-results')
        rurl1 = bilgi.find("a",attrs={"class":"unset"})
        rurl = rurl1.get("href")
        if 'https://' in rurl:
            i = requests.get(rurl)
            c = BeautifulSoup(i.content, "lxml")
            LOGGER.info(c)
            b = c.find('section', id='topSection')
            LOGGER.info(b)
            r = b.find("img")
            t = b.find("score-board")
            audpuan = t.get("audiencescore")
            rating = t.get("rating")
            tompuan = t.get("tomatometerscore")
            isim = t.find("h1")
            fb = t.find("p")
            mes = f"**İsim**: {isim}\n\n**Bilgi**: {fb}\n\n**Audience Puanı**: {audpuan}\n\n**Tomatometer Puanı**: {tompuan}\n\n**İzleyici Kitlesi**: {rating}"
            LOGGER.info(t)
            rresim = r.get("src")
            gresim = rresim.replace("206x305", "1632x2440")
            if 'https://' in gresim:
                await message.reply_photo(
                    photo=gresim, 
                    caption=mes)
            else:
                await message.reply_text(mes)
        else:
            await message.reply_text("Bulamadım..")
    except Exception as e:
        await message.reply_text(e)
 
