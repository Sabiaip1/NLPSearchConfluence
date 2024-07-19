import telebot
from telebot import types
from ElasticSearch import interactive_search

bot = telebot.TeleBot('BOT-TOKEN')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "Привет! Я бот-помощник по Confluence ПЭК!\nПросто введи свой вопрос, и я найду подходящие страницы.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text != '':
        response = interactive_search(message.text)
        bot.send_message(message.from_user.id, response, parse_mode='Markdown')

bot.polling(none_stop=True, interval=0) 