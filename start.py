from telebot import *

bot = TeleBot('6123239125:AAFrcgVlnt5tgzGUTwyxCaXdsQhmtU6shi0')

@bot.message_handler(commands=['start'])
def start(message):
    chseKey = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Жми!')
    chseKey.add(btn)
    bot.send_message(message.from_user.id, 'Жми, чтобы узнать, какой ты Арсений!', reply_markup=chseKey)
    