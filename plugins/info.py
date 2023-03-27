from pyrogram import Client, filters
import logging
from pyrogram.types import InputMediaPhoto
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command('bilgi'))
async def info(bot, message):
    try:
        if message.reply_to_message:
            text = message.from_user
            if text.is_premium == False:
                pre = "Normal Üye"
            else:
                pre = "Premium Üye" 
            async for photo in bot.get_chat_photos(message.reply_to_message.from_user.id, limit=1):
                LOGGER.info(photo)
                caption = f"**Adı**: {message.reply_to_message.from_user.first_name}\n**Durum**: {pre}\n**Kullanıcı Adı**: @{message.reply_to_message.from_user.username}\n**Id**: `{message.reply_to_message.from_user.id}`\n**Dc Id**: {message.reply_to_message.from_user.dc_id}\n**O**: {message.reply_to_message.from_user.mention}"
                await message.reply_photo(photo.file_id, caption=caption) 
        else:
            return
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('foto'))
async def forogetir(bot, message):
    try:
        if not message.reply_to_message:
            await message.reply_text("`Lütfen Birini Yanıtla..`")
            return
        messplit = message.text.split(" ")
        if len(messplit) == 1:
            limit = 1
            sayi = 0
        else:
            limit = messplit[1]
            sayi = int(limit) - 1
        fotolar = [] 
        say = 0
        async for photo in bot.get_chat_photos(message.reply_to_message.from_user.id, limit=int(limit)):
            if int(say) == int(sayi):
                await message.reply_photo(photo.file_id)
                return
            else:
                say +=1
    except Exception as e:
        await message.reply_text(e)


@Client.on_message(filters.command('fotolar'))
async def forolargetir(bot, message):
    try:
        if not message.reply_to_message:
            await message.reply_text("`Lütfen Birini Yanıtla..`")
            return
        fotolar = [] 
        say = 0
        async for photo in bot.get_chat_photos(message.reply_to_message.from_user.id):
            if len(fotolar) == 10:
                await message.reply_media_group(fotolar)
                fotolar = []
            fotolar.append(InputMediaPhoto(photo.file_id))
        if len(fotolar) > 0:
            await message.reply_media_group(fotolar)
    except Exception as e:
        await message.reply_text(e)
