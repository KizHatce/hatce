from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command('puhu'))
async def puhutv(bot, message):
    try:
        url = "https://puhutv.com/fi-1-bolum-izle"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        LOGGER.info(c)
    except Exception as e:
        await message.reply_text(e)
