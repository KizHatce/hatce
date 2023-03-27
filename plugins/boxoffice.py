from pyrogram import Client, filters
import requests
import logging
from bs4 import BeautifulSoup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
 
tumzamanlarurl = "https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW&ref_=bo_cso_ac"
dunyarurl = "https://www.boxofficemojo.com/year/world/?ref_=bo_nb_hm_tab"
trurlurl = "https://www.boxofficemojo.com/weekend/by-year/2023/?area=TR"
dunya = ["dunya", "d", "Dünya", "dünya", "world"] 
turkiye = ["turkiye", "turkey", "t", "türkiye", "turk", "türk"]

@Client.on_message(filters.command('gise'))
async def tumgise(bot, message):
    try:
        t = message.text.split(" ")
        if len(t) < 2:
            s = "al"
        else:
            s = t[1]
        if s in turkiye:
            try:
                istek = requests.get(trurlurl)
                corba = BeautifulSoup(istek.content, "lxml")
                bilgi = corba.find('div', id='table')
                LOGGER.info(bilgi) 
                tumu = []
                text = f"**Türkiye Güncel Gişe Durumu**:\n\n" 
                say = 0
                for bak in bilgi.findAll('tr')[1:]:
                    link = (None if bak.find('a', attrs={"class":"a-link-normal"}) is None else bak.find('a', attrs={"class":"a-link-normal"}))
                    href = link.get("href")
                    trurl = f"https://www.boxofficemojo.com{href}"
                    istek1 = requests.get(trurl)
                    corba1 = BeautifulSoup(istek1.content, "lxml")
                    bilgi1 = corba1.find('div', id='table')
                    LOGGER.info(bilgi1) 
                    say = 0
                    trtext = f"**Türkiye {link} Haftasındaki Güncel Gişe**:\n\n"
                    for i in bilgi1.findAll('tr')[1:]: 
                        isim = i.find('td', attrs={"class":"a-text-left mojo-field-type-release mojo-cell-wide"}).text if i.find('td', attrs={"class":"a-text-left mojo-field-type-release mojo-cell-wide"}) else None
                        para = (None if i.find('td', attrs={"class":"a-text-right mojo-field-type-money mojo-estimatable"}) is None else i.find('td', attrs={"class":"a-text-right mojo-field-type-money mojo-estimatable"}).text)
                        say += 1
                        trtext += f"{say}-) {isim} - **Kazanılan Para**: {para}\n\n"
                        if int(say) == 5:
                            await message.reply_text(trtext)
                            return
            except Exception as e:
                await message.reply_text(e)
        elif s in dunya:
            try:
                istek = requests.get(dunyarurl)
                corba = BeautifulSoup(istek.content, "lxml")
                bilgi = corba.find('div', id='table')
                LOGGER.info(bilgi) 
                tumu = []
                text = f"**Tüm Dünya Güncel Gişe Durumu**:\n\n" 
                say = 0
                for bak in bilgi.findAll('tr')[1:]:
                    isim = bak.find('td', attrs={"class":"a-text-left mojo-field-type-release_group"}).text if bak.find('td', attrs={"class":"a-text-left mojo-field-type-release_group"}) else None
                    para = (None if bak.find('td', attrs={"class":"a-text-right mojo-field-type-money"}) is None else bak.find('td', attrs={"class":"a-text-right mojo-field-type-money"}).text)
                    say += 1
                    text += f"{say}-) {isim} - {para}\n\n"
                    if int(say) == 5:
                        await message.reply_text(text)
                        return
            except Exception as e:
                await message.reply_text(e)
        else:
            istek = requests.get(tumzamanlarurl)
            corba = BeautifulSoup(istek.content, "lxml")
            bilgi = corba.find('div', id='table')
            LOGGER.info(bilgi) 
            tumu = []
            text = f"**Tüm Zamanlar Gişe Durumu**:\n\n" 
            say = 0
            for bak in bilgi.findAll('tr')[1:]:
                isim = bak.find('td', attrs={"class":"a-text-left mojo-field-type-title"}).text if bak.find('td', attrs={"class":"a-text-left mojo-field-type-title"}) else None
                para = (None if bak.find('td', attrs={"class":"a-text-right mojo-field-type-money"}) is None else bak.find('td', attrs={"class":"a-text-right mojo-field-type-money"}).text)
                say += 1 
                text += f"{say}-) {isim} - {para}\n\n"
                if int(say) == 5:
                    await message.reply_text(text)
                    return
    except Exception as e:
        await message.reply_text(e)
