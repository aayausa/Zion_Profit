const TelegramBot = require("node-telegram-bot-api");
require("dotenv").config();

const token = process.env.BOT_TOKEN;
const bot = new TelegramBot(token, { polling: true });

const steps = [
  "🔹 Шаг 1: Добро пожаловать! Нажми, чтобы продолжить.",
  "🔹 Шаг 2: Вот следующий шаг.",
  "🔹 Шаг 3: Почти готово!",
  "✅ Шаг 4: Готово! Спасибо, что прошёл все шаги."
];

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, "Привет! Начнём с шага 1:", {
    reply_markup: {
      inline_keyboard: [[{ text: "Перейти к шагу 1", callback_data: "step_0" }]]
    }
  });
});

bot.on("callback_query", (callbackQuery) => {
  const msg = callbackQuery.message;
  const chatId = msg.chat.id;
  const data = callbackQuery.data;

  const stepIndex = parseInt(data.split("_")[1]);
  const text = steps[stepIndex];

  let reply_markup = undefined;
  if (stepIndex + 1 < steps.length) {
    reply_markup = {
      inline_keyboard: [[{ text: "Далее ➡️", callback_data: `step_${stepIndex + 1}` }]]
    };
  }

  bot.editMessageText(text, {
    chat_id: chatId,
    message_id: msg.message_id,
    reply_markup
  });
});
