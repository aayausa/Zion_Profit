import telegram
from telegram.ext import Application, CommandHandler

BOT_TOKEN = "7749144104:AAGNwAayxnerJY-pSe0dR4y4YuKplDiuq9E"

async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Вот ваше видео:"
    )
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video="URL_ВАШЕГО_ВИДЕО"
    )

application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.run_polling()
