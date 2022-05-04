# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:

# 00 на zero;
# 11 на one;
# 22 на two;
# 33 на three;
# 44 на four;
# 55 на five;
# 66 на six;
# 77 на seven;
# 88 на eight;
# 99 на nine.
# Формат входных данных
# На вход программе подается натуральное число.

# Формат выходных данных
# Программа должна вывести строковое представление числа.

# Примечание. Используйте словарь вместо условного оператора.

# Тестовые данные 🟢
# Sample Input 1:

# 230
# Sample Output 1:

# two three zero
# Sample Input 2:

# 7
# Sample Output 2:

# seven
# Sample Input 3:

# 11111111
# Sample Output 3:

# one one one one one one one one
# Sample Input 4:

# 83
# Sample Output 4:

# eight three


dictionary = {  #  словарь числа == слова
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}  
n = input()  #  ввод в значение str
lists = []  #  список для разделения nnn на n n n 
lists_text = []  #  список   n == text
for i in range(len(n)):  #  цикл, для разделения nnn на n n n 
    a = n[i]  #  пока комментил, понял что можно в одну строку lists.append(n[i])
    lists.append(a)  #  добавление в список
    
for j in lists:  #  цикл для n == text
    lists_text.append(dictionary[j])  #  добавляем в словарь
print(' '.join(lists_text))  #  печатаем словарь, который собран в строку через пробел