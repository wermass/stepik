# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. 
# Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# это даны списки слов
n = s.split()  #  переводим всё в словарь
result = {}  #  создаем словарь для подсчета вхождений
sum1 = {}  #  словарь, с наибольшими кол-ми вхождеий
for i in n:   #  цикл, добавляющий в словарь ключ -слово из списка, значение- кол-во повторений
    result[i] = result.get(i, 0) +1   #  если ключа нет, создаем со значением ноль и добавляем к нему 1, если есть, то добавляем к нему 1

g = max(result)  #  это я просто эксперементировал как отреагирует max() на словарь
h = result.values()  #  создал строку, где есть все значение словаря result
o = max(h)  #  вывело максимальное число из значений словаря result
for j in result:  #  создал спасиок, который перечисляет все значения словаря result
    
    a = result[j]  #  для удоства обозначил значение переменной (я так понимаю лишний шаг, за то непутался)
    if a >= o:  #  если значение больше или равно (хотя можно было просто равно) максимальному значению из словаря, то
        
        sum1.setdefault(j, result[j])  #  добавляем список ключ \ значение в словарь sum1
        
t = min(sum1)  #  находим минимальный ключ( проверив на g, работает)
print(t)  #  выводим на экран требуемое