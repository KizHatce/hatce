import os
import logging
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
import time
from pyrogram.raw.all import layer
import pyrogram
from pyrogram import Client, __version__
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
botStartTime = time.time()

plugins = dict(root='plugins')


class Bot(Client):

    def __init__(self):
        super().__init__(
            name='multivideobot',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=343,
            plugins=plugins,
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        owner = await self.get_chat(OWNER_ID)
        print(owner)
        me = await self.get_me()
        self.username = '@' + me.username
        LOGGER.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}. Premium {me.is_premium}.")
        if OWNER_ID != 0:
            try:
                await self.send_message(text="Karanlığın küllerinden yeniden doğdum.",
                    chat_id=OWNER_ID)
            except Exception as t:
                LOGGER.error(str(t))

    async def stop(self, *args):
        if OWNER_ID != 0:
            texto = f"Son nefesimi verdim."
            try:
                await self.send_document(document='log.txt', caption=texto, chat_id=OWNER_ID)
            except Exception as t:
                LOGGER.warning(str(t))
        await super().stop()
        LOGGER.info(msg="App Stopped.")
        exit()

app = Bot()
app.run()
