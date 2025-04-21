import os
import telegram
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")
VIDEO_URL = os.getenv("VIDEO_URL")

async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Вот ваше видео:"
    )
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=VIDEO_URL
    )

application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.run_polling()
