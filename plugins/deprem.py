from pyrogram import Client, filters 
import json 
import requests 
from unidecode import unidecode

url = "https://hasanadiguzel.com.tr/api/sondepremler"

@Client.on_message(filters.command("deprem"))
async def deprembilgi(bot, message):
    try:
        link = unidecode(message.text).split()
        if len(link) == 1:
            sayi = 1
        else:
            sayi =  link[1]
        print(sayi)
        say = 0
        response = requests.get(url)
        data = response.json()
        bilgi = data['data']
        text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
        for i in bilgi:
            say += 1
            latitude1 = f"{i['enlem_n']}"
            longitude1 = f"{i['boylam_e']}"
            dadresurl = 'https://maps.google.com/maps?q=' + latitude1 + ',' + longitude1
            text += f"{say}-)\nBüyüklük: {i['ml']}\nDerinlik: {i['derinlik_km']}\nLokasyon: [{i['yer']}]({dadresurl})\nTarih: {i['tarih']} {i['saat']}\n\n"
            if say == int(sayi):
                await bot.send_message(
                    chat_id=message.chat.id, 
                    text=text) 
                return
    except Exception as e:
        await message.reply_text(e) 
