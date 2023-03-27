# CODED BY :d

import pyrogram
from pyrogram import Client, filters
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ChatMemberUpdated

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.group & filters.service & filters.new_chat_members)
async def hosveyabos(bot, message):
    try:
        LOGGER.info(message.new_chat_members)
        idseyi = message.new_chat_members
        idtext = "{}".format(*idseyi) 
        id1 = idtext.split('"id": ')[1]
        kisiid = id1.split(',')[0] 
        yenikanal = await bot.get_chat(message.chat.id)
        LOGGER.info(kisiid) 
        botid = 5708287366
        LOGGER.info(botid)
        if int(kisiid) == int(botid):
            await bot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/5ea51a7229254f84767f6.jpg",
                caption='Bu gruba beni eklediğin için teşekkürler. Kullanım için /start yazabilirsin.')
            await bot.send_message(OWNER_ID, f"#YeniKanalEklenmesi\n\n\n**Kanal Adı**: {yenikanal.title}\n**Kanal id**: {yenikanal.id}\n**Ekleyen**: {message.from_user.first_name}\n**Ekleyen id**: {message.from_user.id}\n\nEğer bu kanalı sevmediysen `/ayril {yenikanal.id}` komutu ile botu Çıkartabilirsin..")
    except Exception as e:
        await bot.send_message(chat_id=OWNER_ID, text=e)

@Client.on_message(filters.command('ayril'))
async def baybay(bot, message):
    try:
        text = message.text.split(" ", 1)
        id = text[1]
        k = await bot.get_chat(id)
        m = await bot.send_photo(
            chat_id=id, 
            photo="https://telegra.ph/file/b9099e8d2f4a7075ec395.jpg",
            caption="Sahibim Bu Kanalda Bulunmamı Onaylamadı Gidiyom Ben..\n\nDestek ile konușabilirsin.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Destek", url="https://t.me/mmagneto")]]))
        try:
            m.pin()
        except Exception:
            pass
        await bot.leave_chat(id)
        await message.reply_text(f"Bașarıyla {k.title} Kanalından Çıkıldı")
    except Exception as e:
        await message.reply_text(e)
