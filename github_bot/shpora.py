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