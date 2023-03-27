# CODED BY :d
from pyrogram.types import InputMediaAudio
from pyrogram import Client, filters
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch
import pytube
import asyncio

async def indirmuzik(link, title):
    download_directory = f"downloads/{title}.m4a"
    command_to_exec = [
        "yt-dlp",
        "-c",
        "--embed-subs",
        "-f", "bestaudio[ext=m4a]",
        "--hls-prefer-ffmpeg", link,
        "-o", download_directory
    ]
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    return download_directory


@Client.on_message(filters.command('muzik'))
async def muzikk(bot, message):
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        text = message.text.split(" ", 1)
        if len(text) < 2:
            await message.reply_text("Hatalı Kullanım..\n\nDoğrusu: `/muzik Kalbin Yok mu Senin? `")
            return
        else:
            m = await message.reply_text("`Arıyorum..`") 
            aranacak = text[1]
            results = YoutubeSearch(aranacak, max_results=1).to_dict()
            if results:
                link = f"https://youtube.com{results[0]['url_suffix']}"
                title = results[0]["title"]
                thumbnail = results[0]["thumbnails"][0]
                duration = results[0]["duration"]
                views = results[0]["views"]
                thumb_name = f'thumb{message.id}.jpg'
                thumb = requests.get(thumbnail, allow_redirects=True)
                open(thumb_name, 'wb').write(thumb.content)
                await m.edit("`Buldum Indiriyorum...`")
                audio_file = await indirmuzik(link, title)
                rep = f"[İndirildi](https://t.me/iftarSahurTrRoBot)"
                carp, durationn, dur = 1, 0, duration.split(':')
                for i in range(len(dur)-1, -1, -1):
                    durationn += (int(dur[i]) * carp)
                    carp *= 60
                await m.edit("`Yüklüyorum..`")
                await bot.send_audio(
                    chat_id=message.chat.id,
                    audio=audio_file, 
                    thumb=thumb_name,
                    duration=durationn,
                    performer="@iftarSahurTrRobot", 
                    caption=rep)
                await m.delete()
            else:
                await m.edit("`İstediğini Bulamadım 🥱`")
    except Exception as e:
        await message.reply_text(e)


@Client.on_message(filters.command('playlist'))
async def playlist(bot, message):
    muzikler = []
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        m = await message.reply_text("`Arıyorum..`")
        text = message.text.split(" ", 1)
        url = text[1]
        playlist = pytube.Playlist(url)
        urls1 = playlist.video_urls
        text = ""
        for url in urls1:
            text += f"{url}\n"
        txtdosya = f"{message.chat.id}.txt"
        with open(txtdosya, 'w') as _urller:
            _urller.write(text)
        await message.reply_document(txtdosya)
        for mp in open(txtdosya, 'r', encoding="latin-1"):
            link = mp.split(' ')[0]
            results = YoutubeSearch(link, max_results=1).to_dict()
            if results:
                link = f"https://youtube.com{results[0]['url_suffix']}"
                title = results[0]["title"]
                thumbnail = results[0]["thumbnails"][0]
                duration = results[0]["duration"]
                views = results[0]["views"]
                thumb_name = f'thumb{message.id}.jpg'
                thumb = requests.get(thumbnail, allow_redirects=True)
                open(thumb_name, 'wb').write(thumb.content)
                await m.edit(f"`{title} Indiriliyor...`")
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(link, download=False)
                    audio_file = ydl.prepare_filename(info_dict)
                    ydl.process_info(info_dict)
                rep = f"[İndirildi](https://t.me/iftarSahurTrRoBot)"
                carp, durationn, dur = 1, 0, duration.split(':')
                for i in range(len(dur)-1, -1, -1):
                    durationn += (int(dur[i]) * carp)
                    carp *= 60
                await m.edit(f"`{title} Yükleniyor..`")
                await bot.send_audio(
                    chat_id=message.chat.id,
                    audio=audio_file, 
                    thumb=thumb_name,
                    duration=durationn,
                    caption=rep)
            else:
                await m.edit("`İstediğini Bulamadım 🥱`")
    except Exception as e:
        await message.reply_text(e)
