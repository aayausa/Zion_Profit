from flask import Flask, request
import os
import telegram

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")
VIDEO_URL = os.getenv("VIDEO_URL")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route("/", methods=["POST"])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="Привет! Вот ваше видео:")
        bot.send_video(chat_id=chat_id, video=VIDEO_URL)
    return "OK"

if __name__ == "__main__":
    WEBHOOK_URL = f"https://{os.getenv('RAILWAY_APP_DOMAIN')}/"
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
