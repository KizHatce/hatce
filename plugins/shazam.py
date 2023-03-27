from pyrogram import Client, filters
from shazamio import Shazam
import json
import telegraph
from telegraph import Telegraph
import requests
import os, requests, time


telegraph = Telegraph()
telegraph.create_account(short_name='ShazamBot')

@Client.on_message(filters.command('shazam'))
async def shazamtara(bot, message):
    try:
        if not message.reply_to_message:
            await message.reply_text("`Bir ses veya videoyu yanıtla...`")
        elif message.reply_to_message.audio or message.reply_to_message.video:
            mes = await message.reply_text("`Shazamda Arıyorum...`")
            ses = await bot.download_media(
                message = message.reply_to_message,
                file_name = f"{message.chat.id}.mp3")
            splitpath = ses.split("/downloads/")
            sestemp = splitpath[1]
            aranacak = f"downloads/{sestemp}"
            shazam = Shazam()
            out = await shazam.recognize_song(aranacak)
            await mes.edit("`Buldum Bilgileri Getiriyorum..`") 
            bilgi = json.dumps(out)
            bilgiler = json.loads(bilgi)
            print(bilgiler)
            i = bilgiler["track"]
            try:
                photo = f"{i['images']['coverart']}"
            except:
                pass
            lyrics = f"{i['sections'][1]['text']}"
            print(lyrics)
            satir = "\n"
            try:
                sarki = f"{i['title']}"
            except:
                pass
            try:
                unlu = f"{i['subtitle']}"
            except:
                pass 
            try:
                shazamid = f"{i['key']}"
            except:
                pass
            link = telegraph.create_page(
                    f"{sarki} Sözleri :d",
                    html_content=lyrics)
            text = f"**Şarkı**: [{i['title']}]({i['share']['href']})\n**Sanatçı**: {i['subtitle']}\n**Shazam İd**: {shazamid}\n**Lyrics**: {link['url']}"
            if photo:
                await bot.send_photo(
                    chat_id = message.chat.id, 
                    photo = photo, 
                    caption = text)
                await mes.delete()
            else:
                await message.reply_text(text)
                await mes.delete()
    except Exception as e:
        await message.reply_text(e)
