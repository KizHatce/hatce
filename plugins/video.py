from pyrogram import Client, filters
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch
import asyncio
import ffmpeg
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import pytube
from youtube_video_scraping import *
import time
import math
PRGRS = {}

import logging
from bs4 import BeautifulSoup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

async def progress_bar(current, total, text, message, start):

    now = time.time()
    diff = now-start
    if round(diff % 10) == 0 or current == total:
        percentage = current*100/total
        speed = current/diff
        elapsed_time = round(diff)*1000
        eta = round((total-current)/speed)*1000
        ett = eta + elapsed_time

        elapsed_time = TimeFormatter(elapsed_time)
        ett = TimeFormatter(ett)

        progress = "[{0}{1}] \n**İlerleme**: {2}%\n".format(
            ''.join(["●" for i in range(math.floor(percentage / 10))]),
            ''.join(["○" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "**Indirilen**: {0}/{1}\n**Hız**: `{2}`/s\n**Tahmini Süre**: `{3}`\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            ett if ett != '' else "0 s"
        )

        try :
            await message.edit(
                text = '{}'.format(tmp)
            )
        except:
            pass

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]


def get_thumbnail(in_filename, path, ttl):
    out_filename = os.path.join(path, str(time.time()) + ".jpg")
    open(out_filename, 'a').close()
    try:
        (
            ffmpeg
            .input(in_filename, ss=ttl)
            .output(out_filename, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return out_filename
    except ffmpeg.Error as e:
      return None

def get_duration(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("duration"):
      return metadata.get('duration').seconds
    else:
      return 0

def get_width_height(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("width") and metadata.has("height"):
      return metadata.get("width"), metadata.get("height")
    else:
      return 1280, 720


async def indir(link):
    download_directory = "downloads/ytvideo.mp4"
    command_to_exec = [
        "yt-dlp",
        "-c",
        "--embed-subs",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio",
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

@Client.on_message(filters.command('ytvideo'))
async def ytvideooo(bot, message):
    ydl_opts = {"format": "bestvideo[ext=mp4]"}
    try:
        text = message.text.split(" ", 1)
        if len(text) < 2:
            await message.reply_text("Hatalı Kullanım..\n\nDoğrusu: `/ytvideo Yeşil Uzaylı Dansı`")
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
                video = await indir(link)
                rep = f"[İndirildi](https://t.me/iftarSahurTrRoBot)"
                carp, durationn, dur = 1, 0, duration.split(':')
                for i in range(len(dur)-1, -1, -1):
                    durationn += (int(dur[i]) * carp)
                    carp *= 60
                await m.edit("`Yüklüyorum..`")
                user = message.from_user
                caption = f"{title}\n\nVideoyu Isteyen: {user.mention}"
                await bot.send_video(
                    chat_id=message.chat.id,
                    video=video, 
                    thumb=thumb_name,
                    duration=durationn,
                    caption=caption)
                await m.delete()
                os.remove(video)
            else:
                await m.edit("`İstediğini Bulamadım 🥱`")
    except Exception as e:
        await message.reply_text(e) 


@Client.on_message(filters.text)
async def ytvideoindir(bot, message):
    ydl_opts = {"format": "bestvideo[ext=mp4]"}
    try:
        text = message.text.split(" ", 1)
        if ["youtube.com", "youtu.be"] in message.text:
            m = await message.reply_text("`İndiriyorum..`")
            link = message.text
            video = await indir(link) 
            await m.edit("`Yüklüyorum..`")
            user = message.from_user
            caption = f"Videoyu Isteyen: {user.mention}"
            duration = get_duration(video)
            DOWNLOAD_DIR = "downloads"
            thumb = get_thumbnail(video, './' + DOWNLOAD_DIR, duration / 4)
            width, height = get_width_height(video)
            start_time=time.time()
            await bot.send_video(
                chat_id=message.chat.id,
                video=video, 
                thumb=thumb,
                duration=duration,
                width=width, 
                height=height,
                progress = progress_bar, 
                progress_args = (
                    'Yükleniyor!',
                    m,
                    start_time
                    ),
                caption=caption)
            await m.delete()
            os.remove(video)
        else:
            return
    except Exception as e:
        await message.reply_text(e) 


@Client.on_message(filters.command('vplaylist'))
async def vplaylist(bot, message):
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
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=False)
                isim = info_dict["title"]
                LOGGER.info(isim)
            await m.edit(f"`{isim} İndiriliyor..`")
            video = await indir(link) 
            await m.edit("`Yüklüyorum..`")
            user = message.from_user
            caption = f"{isim}"
            duration = get_duration(video)
            DOWNLOAD_DIR = "downloads"
            thumb = get_thumbnail(video, './' + DOWNLOAD_DIR, duration / 4)
            width, height = get_width_height(video)
            start_time=time.time()
            await bot.send_video(
                chat_id=message.chat.id,
                video=video, 
                thumb=thumb,
                duration=duration,
                width=width, 
                height=height,
                progress = progress_bar, 
                progress_args = (
                    'Yükleniyor!',
                    m,
                    start_time
                    ),
                caption=caption)
            os.remove(video)
    except Exception as e:
        await message.reply_text(e)
