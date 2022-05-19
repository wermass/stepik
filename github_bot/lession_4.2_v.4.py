# Напишите бота, который определяет тип сообщения: если вы отправили фото - фото, видео -
# видео, стикер - стикер и т.д.

import telebot

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(content_types=['photo'])
def start(message):
    bot.send_message(message.chat.id, " Это фото")


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, "Это текст")


@bot.message_handler(content_types=['video'])
def start(message):
    bot.send_message(message.chat.id, f"это видео")


@bot.message_handler(content_types=['document'])
def start(message):
    bot.send_message(message.chat.id, f"Это документ")


@bot.message_handler(content_types=['sticker'])
def start(message):
    bot.send_message(message.chat.id, " какой-то смайлик")


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
