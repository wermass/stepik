# м сами поисковые запросы.

# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

# Примечание. Поиск не должен быть чувствителен к регистру символов.

# Тестовые данные 🟢
# Sample Input:

# 5
# Язык Python прекрасен
# C# - отличный язык программирования
# Stepik - отличная платформа
# BEEGEEK FOREVER!
# язык Python появился 20 февраля 1991
# 2
# язык
# python
# Sample Output:

# Язык Python прекрасен
# язык Python появился 20 февраля 1991



n = int(input())
lists = [] # строки
lists_1 = [] # запросы
lists_2 = [] # пересечение
for i in range(n):
    lists.append(input())
k = int(input())
for j in range(k):
    lists_1.append(input())
       
for i in lists:
    sum = 0
    for j in lists_1:
        if i.lower().count(j.lower()) > 0 :
            
            if i not in lists_2:
                sum += 1
                if sum >= k:
                    lists_2.append(i)
    
print(*lists_2, sep='\n')