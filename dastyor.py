import telebot

bot = telebot.TeleBot("7946989792:AAGRiqNPua3ZEIT_iGX_RPV6vKpPoSzHPgU")

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник😉")
    print(message.text)

# Команда /help
@bot.message_handler(commands=['help'])
def help(message):
    help_text = (
        "Команды, которые я поддерживаю:\n"
        "/start - Начать диалог и поприветствовать\n"
        "/help - Получить список доступных команд"
    )
    bot.send_message(message.from_user.id, help_text)

# Запускаем бота
bot.infinity_polling()