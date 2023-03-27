from pyrogram import Client, filters

@Client.on_message(filters.command('at'))
async def atty(bot, message):
    try:
        userid = message.reply_to_message.from_user.id
        await bot.ban_chat_member(message.chat.id, userid)
        await message.reply_text(f"{message.reply_to_message.from_user.mention} {message.chat.title} Grubundan Banlandı..")
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('gerial'))
async def att(bot, message):
    try:
        userid = message.reply_to_message.from_user.id
        await bot.unban_chat_member(message.chat.id, userid)
        await message.reply_text(f"{message.reply_to_message.from_user.mention} {message.chat.title} Grubundaki Banı Açıldı..")
    except Exception as e:
        await message.reply_text(e)
