# Маша хочет проверять сообщения пользователей на палиндромы. Если сообщение является палиндромом - функция должна вернуть True и обработчик сработает, иначе - False. Функция должна быть независимой от регистра, и не должна учитывать: пробелы, ь, ъ. Напишите только саму функцию, ничего другого делать не нужно, даже вызывать её.
# 
# Sample Input 1:
# 
# шалаш
# Sample Output 1:
# 
# True
# Sample Input 2:
# 
# шакал
# Sample Output 2:
# 
# False
# Sample Input 3:
# 
# Искать такси
# Sample Output 3:
# 
# True
# Sample Input 4:
# 
# Ночное молчанье
# Sample Output 4:
# 
# False
# 
# import telebot
# 
# API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
# bot = telebot.TeleBot(API_TOKEN)
# 
# 
# @bot.message_handler(content_types=['photo'])
# def start(message):
#     bot.send_message(message.chat.id, " Это фото")
# 
# 
# @bot.message_handler(content_types=['text'])
# def start(message):
#     bot.send_message(message.chat.id, "Это текст")
# 
# 
# @bot.message_handler(content_types=['video'])
# def start(message):
#     bot.send_message(message.chat.id, f"это видео")
# 
# 
# @bot.message_handler(content_types=['document'])
# def start(message):
#     bot.send_message(message.chat.id, f"Это документ")
# 
# 
# @bot.message_handler(content_types=['sticker'])
# def start(message):
#     bot.send_message(message.chat.id, " какой-то смайлик")
# 
# 
# bot.polling()
# 
# # шпора
# # Идентификатор чата - message.chat.id
# # Идентификатор пользователя - message.from_user.id
# # Текст сообщения - message.text
# # Имя - message.from_user.first_name
# # Фамилия - message.from_user.last_name
# # Псевдоним - message.from_user.username
# # Тип чата - message.chat.type
# # Идентификатор сообщения - message.id
# # Тип контента сообщения - message.content_type


import re


def palindrom(word):
    #Код писать сюда \(❤‿❤)/
    word = word.lower()
    symbols = [' ', 'ь', 'ъ']
    for chek in symbols:
        #print('chek  ', chek)
        for text in word:
            #print('text   ', text)
            if text in symbols:
                word = re.sub(text, '', word)
            
    #print('word   ', word)    
    back = "". join(reversed(word))
    flag = True
   
    if word == back:
        flag = True
    else:
        flag = False
    return flag    
