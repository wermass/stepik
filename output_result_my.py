# На вход программе подается строка генетического кода,
# состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). 
#Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
# пример:
# Sample Input 1:
#
#АааГГЦЦцТТттт
#Sample Output 1:
#
#Аденин: 3
#Гуанин: 2
#Цитозин: 3
#Тимин: 5

n = input().lower()

print('Аденин:', n.count('а'))
print('Гуанин:', n.count('г'))
print('Цитозин:', n.count('ц'))
print('Тимин:', n.count('т'))