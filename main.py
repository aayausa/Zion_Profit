from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

steps = [
    "🔹 Шаг 1: Добро пожаловать! Нажми, чтобы продолжить.",
    "🔹 Шаг 2: Вот следующий шаг.",
    "🔹 Шаг 3: Почти готово!",
    "✅ Шаг 4: Готово! Спасибо, что прошёл все шаги."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Перейти к шагу 1", callback_data="step_0")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми кнопку ниже, чтобы начать:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    step_index = int(query.data.split("_")[1])
    text = steps[step_index]

    if step_index + 1 < len(steps):
        keyboard = [[InlineKeyboardButton("Далее ➡️", callback_data=f"step_{step_index + 1}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        reply_markup = None

    await query.edit_message_text(text=text, reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("✅ Бот запущен")
app.run_polling()
