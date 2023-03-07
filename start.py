from telebot import *
import random
bot = TeleBot('6123239125:AAFrcgVlnt5tgzGUTwyxCaXdsQhmtU6shi0')

@bot.message_handler(commands=['start'])
def push(message):
    chseKey = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Жми!')
    chseKey.add(btn)
    bot.send_message(message.from_user.id, 'Жми, чтобы узнать, какой ты Арсений!', reply_markup=chseKey)

@bot.message_handler(func=lambda message: True)
def stickers(file):
    #rnd = str(random.randint(1,9))
    sti = open('stickers/1.webm', 'rb')
    bot.send_sticker('@what_Arseny_are_you_bot', sti)

bot.infinity_polling()