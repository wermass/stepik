# Создайте бота, который отправляет фото или видео пользователей бота администратору.
# Если пользователь отправляет что-то кроме видео, фото, команды /start
# - отправляйте ему сообщение «Это не видео и не фото :(». 

import telebot

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, отправь перед публикаций фото или видео, его проверят наши администраторы')



@bot.message_handler(content_types=['photo'])
def start(message):
    bot.send_photo(5296394682, message.photo[0].file_id)
    bot.send_message(message.chat.id, 'фото отправлено администратору')

@bot.message_handler(content_types=['video'])
def start(message):
    bot.send_video(5296394682, message.video.file_id)
    bot.send_message(message.chat.id, 'видео отправлено администратору')

@bot.message_handler(func=lambda message: True)
def bot_main(message):
    bot.send_message(message.chat.id, 'Это не фото и не видео')



# 5296394682
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
