# Мне кажется эта задача очень хорошо готовит к дальнейшему парсингу=)))))
# Взлом Братства Стали 🌶️
# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, и любезно соглашается помочь им в решении их проблем. Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. Известно, что программисты Братства никогда не оставляют комментарии к коду, и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.

# Формат входных данных
# На первой строке вводится символ решётки и сразу же натуральное число nn — количество строк в программе, не считая первой. Далее следует nn строк кода.

# Формат выходных данных
# Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк. Пустую строку вместо первой строки ввода выводить не надо.

# Тестовые данные 🟢
# Sample Input:

# #12
# print("Введите своё имя")
# name = input()
# print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
# password = input()
# if password == "hoover":
#     print("Здравствуйте, рыцарь", name)         #долой Макнамару
# elif password == "noncr":
#     print("Здравствуйте, паладин", name)
# elif password == "gelios":
#     print("Здравствуйте, старейшина", name)          #Элайджа вперёд
# else:
#     print("Здравствуйте, послушник", name)
# Sample Output:

# print("Введите своё имя")
# name = input()
# print("Введите пароль, если имеется")
# password = input()
# if password == "hoover":
#     print("Здравствуйте, рыцарь", name)
# elif password == "noncr":
#     print("Здравствуйте, паладин", name)
# elif password == "gelios":
#     print("Здравствуйте, старейшина", name)
# else:
#     print("Здравствуйте, послушник", name)


n1 = input()
n2 = n1.index('#')
n = n1[n2+1:]
n = int(n)
s =''

for i in range(n):
    s1 = input()
    count = 0
    if '#' in s1:
        s2 = s1.index('#')
        count += 1
    if count > 0:
        s3 = s1[:s2]
    else:
        s3 = s1
    s += s3.rstrip() + '\n'
    
print(s)

# условные операторы конечно не очень, но для меня понятны, вдальнейшем исправлюсь