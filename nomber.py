# это прям гордость!!!!

# Валидный номер 🌶️🌶️
# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером. Строка текста является корректным телефонным номером если она имеет формат:

# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

# Формат входных данных 
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести «YES» если строка является корректным телефонным номером и «NO» в противном случае.

# Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должны быть правильным.

# Тестовые данные 🟢
# Sample Input 1:

# 7-301-447-5820
# Sample Output 1:

# YES
# Sample Input 2:

# 301-447-5820
# Sample Output 2:

# YES
# Sample Input 3:

# 301-4477-5820
# Sample Output 3:

# NO
# Sample Input 4:

# 3X1-447-5820
# Sample Output 4:

# NO
# Sample Input 5:

# 3014475820
# Sample Output 5:

# NO

n = input()
lists = n.split('-')
sum1 = 0
if n[0] == '7':
    if (n[1] == '-') and (n[5] == '-') and (n[9] == '-'):
    
        for i in range(len(lists)):
            if sum1 > 0:
                break
            for j in lists[i]:
                if j in '0123456789':
                    continue
                else:
                    print("NO")
                    sum1 += 1
                    break
    else:
        sum1 +=1
        print("NO")
    if sum1 == 0:
        print("YES")        

elif (n[3] == '-') and (n[7] == '-'):
    for i in range(len(lists)):
        if sum1 > 0:
            break
        for j in lists[i]:
            if j in '0123456789':
                continue
            else:
                print("NO")
                sum1 += 1
                break
    if sum1 == 0:
        print("YES")            
else:
    print("NO")