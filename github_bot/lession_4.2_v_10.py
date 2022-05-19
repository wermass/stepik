# Создайте бота, который проверяет номер по регулярному
# выражению. Номером считается любая последовательность из 11 цифр.
# Если сообщение не является номером - выводите текст: "Отправьте номер телефона",
# иначе выводите: "Это номер телефона".

import telebot

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(regexp= r"\d\d\d\d\d\d\d\d\d\d\d")
def start(message):
    bot.send_message(message.chat.id, "Это номер телефона")

@bot.message_handler(func=lambda message: True)
def start(message):
    bot.send_message(message.chat.id, "Отправьте номер телефона")


bot.polling()