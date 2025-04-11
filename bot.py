import telebot

TOKEN = 7567621284:AAGcl41NapdhBfsU4LvSrVMC_GR2tXqJoSE
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Warzone бот. Пиши /meta — покажу топ комплекты!")

@bot.message_handler(commands=['meta'])
def meta(message):
    bot.send_message(message.chat.id, "Пока что я учусь. В будущем тут будет мета оружия из Warzone.")

bot.polling()