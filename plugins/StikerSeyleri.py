from pyrogram import Client, filters 
from PIL import Image
import os
import re
import asyncio

async def videotostic(video):
    output_vid = "gif.mp4"
    output = f"downloads/{output_vid}"
    command = [
        "ffmpeg",
        "-i",
        video,
        "-map",
        "0:v",
        "-c:v",
        "copy",
        "-y", 
        output
    ]
    process = None
    try:
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        return output
    except Exception as e:
        LOGGER.info(e)

@Client.on_message(filters.command('donustur'))
async def donusturucu(bot, message):
    user_id = message.from_user.id
    message_id = message.reply_to_message.id
    name_format = f"Mickey_{user_id}_{message_id}"
    if message.reply_to_message.photo:
        m = await message.reply_text("`Dönüştürülüyor...`")
        image = await bot.download_media(
                    message = message.reply_to_message,
                    file_name=f"{name_format}.jpg")
        await m.edit("`Gönderiyorum...`")
        im = Image.open(image).convert("RGB")
        im.save(f"{name_format}.webp", "webp")
        sticker = f"{name_format}.webp"
        await m.reply_sticker(sticker)
        await m.delete()
        os.remove(sticker)
        os.remove(image)
    elif message.reply_to_message.video:
        m = await message.reply_text("`Dönüştürülüyor...`")
        name_format = f"downloads/donusturulmussticker"
        image = await bot.download_media(
                    message = message.reply_to_message,
                    file_name=f"{name_format}.webm")
        await m.edit("`Gönderiyorum...`")
        video = f"{name_format}.webm"
        try:
            gif = await videotostic(video) 
            await bot.send_video(
                 chat_id=message.chat.id,
                 video=gif)
            await m.delete()
            os.remove(gif)
            os.remove(video)
        except Exception as e:
            await message.reply_text(e)
    elif message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated == True:
            try:
                name_format = "downloads/donusturulmusvideo"
                gif = await bot.download_media(
                          message = message.reply_to_message,
                          file_name=f"{name_format}.mp4")
                video = f"{name_format}.mp4"
                await bot.send_video(
                    chat_id = message.chat.id, 
                    video = video) 
            except Exception as e:
                await message.reply_text(e)
        elif message.reply_to_message.sticker.is_video == True:
            try:
                name_format = "downloads/donusturulmusvideo"
                gif = await bot.download_media(
                          message = message.reply_to_message,
                          file_name=f"{name_format}.mp4")
                video = f"{name_format}.mp4"
                await bot.send_video(
                    chat_id = message.chat.id, 
                    video = video) 
            except Exception as e:
                await message.reply_text(e)
        else:
            m = await message.reply_text("`Dönüştürülüyor...`")
            sticker = await bot.download_media(
                          message = message.reply_to_message,
                          file_name=f"{name_format}.webp")
            await m.edit("`Gönderiyorum...`")
            im = Image.open(sticker).convert("RGB")
            im.save(f"{name_format}.jpg", "jpeg")
            image = f"{name_format}.jpg"
            await m.reply_photo(image)
            await m.delete()
            os.remove(image)
            os.remove(sticker) 
