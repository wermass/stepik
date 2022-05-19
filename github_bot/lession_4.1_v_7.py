Саша всех обманул...
# В нескольких банках твоего города произошли подозрительные операции. Саша успел сделать то что хотел, но его поймали и он сдал тебя как соучастника. Если вы будете сотрудничать со следователями, то тебя простят, а Саше уменьшат срок. Оказывается, Сашу завербовали мошенники. Эта компания злодеев призывает простых граждан воровать деньги и отправлять им на счёт. В своих сообщениях они постоянно шифруются. В каждом сообщении злоумышленники оставляют особый знак - название своей компании: "Edinaya Rossiya" и хотя бы один символ из следующих: $¥€. Помогите следователям написать функцию findThieves, которую они вставят в @bot.message_handler().
# 
# Что вам нужно сделать:
# 
# Функция должна возвращать True если сообщение писали мошенники и False если нет.
# После того как вы написали функцию отправьте задание на проверку, ничего запускать или выводить не нужно
# Странные символы, которые используют мошенники - $¥€
# 
# Сообщение является сообщением мошенника если совпадают эти 2 условия.
# 
# Sample Input 1:
# 
# fsociety
# Sample Output 1:
# 
# False
# Sample Input 2:
# 
# Edinaya Rossiya $
# Sample Output 2:
# 
# True
# Sample Input 3:
# 
# Edinaya Rossiya Edinaya Rossiya
# Sample Output 3:
# 
# False
# Sample Input 4:
# 
# $¥€ Рубль упал после 23.02.22 $¥€
# Sample Output 4:
# 
# False
# Sample Input 5:
# 
# $¥€
# Sample Output 5:
# 
# False
# Sample Input 6:
# 
# €Edinaya Rossiya€
# Sample Output 6:
# 
# True
# Sample Input 7:
# 
# ¥Edinaya Rossiya¥
# Sample Output 7:
# 
# True


import re


def findThieves(message):
    #Код писать сюда \(❤‿❤)/
    message = message.text
    symbols = ['$', '¥' , '€']
    flag = False
    code_words = ['Edinaya', 'Rossiya']
    count = 0
    for clean in message:
        if clean in symbols:
            message = re.sub(clean, '', message)
            flag = True
    message_list = message.split()
    #print('+++ message   ', message)
    #print('=== message_list   ', message_list)
    if flag == True:
        flag = False
        count = 0
        for clean_two in message_list:
            if clean_two in code_words:
                
                count += 1
                if count >= 2:
                    flag = True
                
    return flag
    
    
    
# почему я недодумался до того решения=))) его подсмотрел после выполнения:

#def findThieves(m):
#     if 'Edinaya Rossiya' in m and ('$'or'¥'or'€') in m:
#         return "True"
#     return "False"    