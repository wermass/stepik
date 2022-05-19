Виды обработчиков
Существует множество видов обработчиков. Большинство из них довольно специфичные и редко используются, в этом курсе будут использованы только 3 вида обработчиков. Но остальные вам следует знать, так как в будущем могут понадобиться:

 

Message handler

Обратывает сообщения, мы уже его прошли.

@bot.message_handler(filters) # <- передаёт объект Message в вашу функцию
 
Edited Message handler
Обрабатывает отредактированные сообщения. Скоро его пройдём.

@bot.edited_message_handler(filters) # <- передаёт объект Message в вашу функцию
 
Channel Post handler
Обрабатывает сообщения каналов.

@bot.channel_post_handler(filters) # <- передаёт объект Message в вашу функцию
 
Edited Channel Post handler
Обрабатывает отредактированные сообщения каналов

@bot.edited_channel_post_handler(filters) # <- передаёт объект Message в вашу функцию
 
Callback Query Handler
Обрабатывает callback запросы. Это мы пройдём позже в уроке кнопки.

@bot.callback_query_handler(func=lambda call: True) # <- передаёт объект CallbackQuery в вашу функцию
 
Shipping Query Handler
Обрабатывает shipping запросы.

@bot.shipping_query_handeler() # <- передаёт объект ShippingQuery в вашу функцию
 
Pre Checkout Query Handler
Обрабатывает pre checkout запросы

@bot.pre_checkout_query_handler() # <- передаёт объект PreCheckoutQuery в вашу функцию
 
Poll Handler
Обрабатывает обновления опросов

@bot.poll_handler() # <- передаёт объект Poll в вашу функцию
 
Poll Answer Handler
Обрабатывает ответы на опросы

@bot.poll_answer_handler() # <- передаёт объект PollAnswer в вашу функцию
 
My Chat Member Handler
Обрабатывает обновления статуса участника бота в чате

@bot.my_chat_member_handler() # <- передаёт объект ChatMemberUpdated в вашу функцию
 
Chat Member Handler
Обрабатывает обновления статуса пользователя в чате

@bot.chat_member_handler() # <- передаёт объект ChatMemberUpdated в вашу функцию
 
Chat Join Request Handler
Обрабатывает запросы на присоединение к чату

@bot.chat_join_request_handler() # <- передаёт объект ChatInviteLink в вашу функцию
 


# Идентификатор чата - message.chat.id
# Идентификатор пользователя - message.from_user.id
# Текст сообщения - message.text
# Имя - message.from_user.first_name
# Фамилия - message.from_user.last_name
# Псевдоним - message.from_user.username
# Тип чата - message.chat.type
# Идентификатор сообщения - message.id
# Тип контента сообщения - message.content_type


У объекта Message также есть аттрибут content_type, который определяет тип сообщения. 
content_type может быть одним из следующих: text, audio, document, photo, sticker, video, video_note, 
voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, 
group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message.

Файлы отправлять можно двумя способами:

Открывать файл и передавать его в метод
Передавать в метод путь к файлу
Мы разберём сразу 2 способа:

import telebot

bot = telebot.TeleBot('token')

# Отправляем фото
photo = open('/tmp/photo.png', 'rb')
bot.send_photo(chat_id, photo)
#или
bot.send_photo(chat_id, "FILEID")

# Отправляем аудио
audio = open('/tmp/audio.mp3', 'rb')
bot.send_audio(chat_id, audio)
#или
bot.send_audio(chat_id, "FILEID")

# Отправляем голосовое сообщение
voice = open('/tmp/voice.ogg', 'rb')
bot.send_voice(chat_id, voice)
#или
bot.send_voice(chat_id, "FILEID")

# Отправляем документ
doc = open('/tmp/file.txt', 'rb')
bot.send_document(chat_id, doc)
#или
bot.send_document(chat_id, "FILEID")

# Отправляем стикер
bot.send_sticker(chat_id, "sticker_id")

# Отправляем видео
video = open('/tmp/video.mp4', 'rb')
bot.send_video(chat_id, video)
#или
bot.send_video(chat_id, "FILEID")
FILEID в примере это путь к файлу. Мы получаем два шаблона для отправки файлов:

Первый способ (Если файл у вас на пк или на хостинге в папке с ботом) Открываем файл и передаём в метод.
Второй способ (Если файл на сайте или у вас есть id файла) Передаём в метод путь к файлу.
Как можно заметить мы можем отправлять любые типы файлов. Отправку остальных типов файлов можете посмотреть тут.

rb - это бинарный режим чтения и записи(read binary), что означает чтение по байтам


parse_mode="HTML"
<b>Жирный</b>, <strong>Жирный</strong>

<i>Курсив</i>, <em>Курсив</em>

<u>Нижнее подчёркивание</u>

<s>Зачёркнутый</s>, <del>Зачёркнутый</del>, <strike>Зачёркнутый</strike>

<a href="https://stepik.org/course/107302/">Гиперссылка</a>

<code>Код</code>

<pre>Моноширинный</pre>

<em>ЧТО ВИДНО  <tg-spoiler>текст спойлера!</tg-spoiler></em>

<tg-spoiler>Спойлер</tg-spoiler>
Пример использования форматированния:
bot.send_message(message.chat.id, 'Это обычный текст, а это <b>Жирный!</b>', parse_mode= "HTML")


Id сообщения пользователя:
Ничего сложного нет. В функции под хендлером получаем сообщение и получаем свойство id:

@bot.message_handler(commands=['start'])
def start(message):
    print(message.id)
Id сообщения бота:
А вот тут уже метод send_message возвращает объект message сообщения, которое мы только что отправили:

@bot.message_handler(commands=['start'])
def start(message):
    bot_message = bot.send_message(message.chat.id, "Отправляю сообщение")
    print(bot_message.id)
    
import time
  time.sleep(1)
  
  
Клавиатура (с условием) (это та, которая выходит в меню, под "введите сообщение")

@bot.message_handler(regexp= r"Купить")
def start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    stone = types.KeyboardButton(text="Камень с глазами")
    back =types.KeyboardButton(text='Назад')
    startKBoard.add(stone, back)
    bot.send_message(message.chat.id, "Что хотите купить?", reply_markup=startKBoard)  
    
    
    
Чтобы убрать клавиатуру в reply_markup нужно передать types.ReplyKeyboardRemove():

bot.send_message(message.chat.id, "Убираем клавиатуру", reply_markup=types.ReplyKeyboardRemove())


Чтобы создать клавиатуру, которая исчезнет при нажатии кнопки, нужно в параметр one_time_keyboard передать True.

Пример создания такой клавиатуры:


from telebot import types



@bot.message_handler(commands=['keyboard'])
def keyboard_start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text="Кнопка 1")
    btn2 = types.KeyboardButton(text="Кнопка 2")
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, "Это одноразовая клавиатура!", reply_markup=kb)




Кнопка используется с клавиатурой InlineKeyboardMarkup, давайте создадим кнопку «Наш сайт»: (это которая находится в тексте)


from telebot import types



@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://stepik.org/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)



Switch-кнопки (перенаправления бота в другой чат) # нахуй это нужно?



from telebot import types



@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)




Callback-кнопки

from telebot import types




@bot.message_handler(commands=['callback'])
def cmd_start(message):
    start_keyboard = types.InlineKeyboardMarkup()
    Hack_Pentagon = types.InlineKeyboardButton(text='Hack Pentagon', callback_data='HackPentagon')
    Snorovka_School = types.InlineKeyboardButton(text='Snorovka School', callback_data='SnorovkaSchool')
    start_keyboard.add(Hack_Pentagon, Snorovka_School)
    bot.send_message(message.chat.id, 'А вот и callback кнопки!', reply_markup=start_keyboard)


#Если получаем callback ответ с клавиатуры запускаем функцию answer_callback
@bot.callback_query_handler(func=lambda c:c.data)
def answer_callback(callback):
    if callback.data == 'SnorovkaSchool':
        #Что-то делаем
    elif callback.data == 'HackPentagon':
        #Взламываем Пентагон



Количество кнопок в строке можно задать с помощью row_width:

start_keyboard = types.InlineKeyboardMarkup(row_width = 1)
Вот так будут выглядеть кнопки при row_width = 1:

Чтобы получить message из callback достаточно написать: callback.message

Теперь мы можем использовать message так, как хотим. Например, после получения callback отправим сообщение:

bot.send_message(callback.message.chat.id,"Ты нажал на кнопку")