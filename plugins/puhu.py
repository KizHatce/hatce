from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
          "content-type": "application/json",
          } 

@Client.on_message(filters.command('puhu'))
async def puhutv(bot, message):
    try:
        url = "https://puhutv.com/yuksek-sosyete-1-bolum-izle"
        r = requests.get(url, headers=headers)
        c = BeautifulSoup(r.content, "lxml")
        LOGGER.info(c)
    except Exception as e:
        await message.reply_text(e)
