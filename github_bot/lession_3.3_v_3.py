import telebot


API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"""id чата: {message.chat.id}\nid пользователя: {message.from_user.id}
Имя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\nПсевдоним: {message.from_user.username}
""")

bot.polling()

# Идентификатор чата - message.chat.id
# Идентификатор пользователя - message.from_user.id
# Текст сообщения - message.text
# Имя - message.from_user.first_name
# Фамилия - message.from_user.last_name
# Псевдоним - message.from_user.username
# Тип чата - message.chat.type
# Идентификатор сообщения - message.id
# Тип контента сообщения - message.content_type