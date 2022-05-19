# Создайте бота, который создаёт файлы с сообщением внутри и отправляет их. Если
# вы не знаете как создавать или отправлять файлы - смотрите подсказку в комментариях.

import telebot
from telebot import types
API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def change_message(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    sell = types.KeyboardButton(text="Товары")
    startKBoard.add(sell)
    bot.send_message(message.chat.id, 'Добро пожаловать в магазин "Полезные товары"', reply_markup=startKBoard)

@bot.message_handler(regexp= r"Купить")
def start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    stone = types.KeyboardButton(text="Камень с глазами")
    back =types.KeyboardButton(text='Назад')
    startKBoard.add(stone, back)
    bot.send_message(message.chat.id, "Что хотите купить?", reply_markup=startKBoard)


@bot.message_handler(regexp= r"Камень")
def start(message):
    photo = open('stone.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bye = types.KeyboardButton(text="Купить")
    back =types.KeyboardButton(text='Назад')
    startKBoard.add(bye, back)
    bot.send_message(message.chat.id, """Товар: Камень с глазами
    Цена 1000$
    В наличии: 2""", reply_markup=startKBoard)

@bot.message_handler(regexp= r"Назад")
def start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    sell = types.KeyboardButton(text="Товары")
    startKBoard.add(sell)
    bot.send_message(message.chat.id, 'Добро пожаловать в магазин "Полезные товары"', reply_markup=startKBoard)

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
