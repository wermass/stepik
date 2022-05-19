# После команды /test бот должен показывать время сообщения.

import telebot
import datetime


API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    date = message.date + 10800  # Прибавляем 3 часа (в секундах) к времени по UTC и получаем время по МСК!
    bot.send_message(message.chat.id, datetime.datetime.utcfromtimestamp(date))

bot.polling()


# шпора
# Идентификатор чата - message.chat.id
# Идентификатор пользователя - message.from_user.id
# Текст сообщения - message.text
# Имя - message.from_user.first_name
# Фамилия - message.from_user.last_name
# Псевдоним - message.from_user.username
# Тип чата - message.chat.type
# Идентификатор сообщения - message.id
# Тип контента сообщения - message.content_type