from config import token
import random
import telebot

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "hello")


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "/start /info /random")


@bot.message_handler(commands=['random'])
def send_random(message):
    bot.reply_to(message, str(random.randint(1,100)))


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'привет':
        bot.reply_to(message, 'пока')
    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()
