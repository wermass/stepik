import pandas as pd
import math


sheet_product = pd.read_excel("trekking3.xlsx", sheet_name=0)
sheet_product.fillna(0, inplace=True)
sheet_raskladka = pd.read_excel("trekking3.xlsx", sheet_name=1)
sheet_raskladka.fillna(0, inplace=True)
sheet_product_znach = {}
sheet_raskladka_name = {}
for product_row in sheet_product.iterrows():
    a = sheet_product_znach.setdefault(product_row[1][0], [product_row[1][1], product_row[1][2],product_row[1][3], product_row[1][4]])

print('== продукты + кортеж кал, белки, жиры, углеводы ==', sheet_product_znach)
dict_numebr_day_kort = {}
for raskladka_row in sheet_raskladka.iterrows():
    # print(raskladka_row[1], '++raskladka_row++')
    numbers_day = raskladka_row[1][0]
    raskladka_product_name = raskladka_row[1][1]
    ves_gram = raskladka_row[1][2]
    # print(numbers_day, raskladka_product_name, ves_gram, sep='!!!\n')
    # print('numbers day   ',numbers_day)  #  номера дней
    # print('raskladka product name   ', raskladka_product_name)
    # print('ves gram   ', ves_gram)

    zapic_bolsh_dict = dict_numebr_day_kort.setdefault(numbers_day, {})
    # print('!!!zapic bolsh dict   ', zapic_bolsh_dict)


    dict_numebr_day_kort[numbers_day].setdefault(raskladka_product_name, 0)
    dict_numebr_day_kort[numbers_day][raskladka_product_name] = dict_numebr_day_kort[numbers_day][raskladka_product_name] + ves_gram


    
    # print('dict_numebr_day_kort[numbers_day]' , dict_numebr_day_kort[numbers_day])
    # product_kkal = sheet_product_kkal[raskladka_name][0] * (raskladka_gram / 100)
    #     product_belk = sheet_product_kkal[raskladka_name][1] * (raskladka_gram/100)
    #     product_jir = sheet_product_kkal[raskladka_name][2] * (raskladka_gram/100)
    #     product_ygl = sheet_product_kkal[raskladka_name][3] * (raskladka_gram/100)

print('== словарь в нем ключь номер дня + словарь ключ название значени вес == ',dict_numebr_day_kort)
for day_slovar in dict_numebr_day_kort:
    # print('== day == ', day_slovar)
    for key_day_slovar in dict_numebr_day_kort[day_slovar]:
        # print('== key day == ', key_day_slovar)
        # print('== обращение к словарю черз день и ключ == ', type(dict_numebr_day_kort[day_slovar][key_day_slovar]))
        # print(' ** ', dict_numebr_day_kort[day_slovar][key_day_slovar]*2)
        # dict_numebr_day_kort[day_slovar][key_day_slovar].append(ves_gram * 2)
        dict_numebr_day_kort[day_slovar][key_day_slovar] = [dict_numebr_day_kort[day_slovar][key_day_slovar] * (sheet_product_znach[key_day_slovar][0]/100), dict_numebr_day_kort[day_slovar][key_day_slovar] * (sheet_product_znach[key_day_slovar][1]/100), dict_numebr_day_kort[day_slovar][key_day_slovar] * (sheet_product_znach[key_day_slovar][2]/100), dict_numebr_day_kort[day_slovar][key_day_slovar] * (sheet_product_znach[key_day_slovar][3]/100)]
print('++ словарь умноженный ккал, белки, жир, углевод.                        ', dict_numebr_day_kort)


total_kkal = {}
total_belk = {}
total_jir = {}
total_ygl = {}


for day_slovar in dict_numebr_day_kort:
    # print('дни словаря  ', day_slovar)
    for product_list in dict_numebr_day_kort[day_slovar]:

        # print('кортеж продуктов   ', dict_numebr_day_kort[day_slovar][product_list])
        kkal_raskl = dict_numebr_day_kort[day_slovar][product_list][0]
        # print('kkal_raskl   ', kkal_raskl)
        total_kkal.setdefault(day_slovar, 0)
        total_kkal[day_slovar] += kkal_raskl

        belk_raskl = dict_numebr_day_kort[day_slovar][product_list][1]
        # print('belk_raskl   ', type(belk_raskl))
        total_belk.setdefault(day_slovar, 0)
        total_belk[day_slovar] += belk_raskl

        jir_raskl = dict_numebr_day_kort[day_slovar][product_list][2]
        # print('kkal_raskl   ', kkal_raskl)
        total_jir.setdefault(day_slovar, 0)
        total_jir[day_slovar] += jir_raskl

        ygl_raskl = dict_numebr_day_kort[day_slovar][product_list][3]
        # print('kkal_raskl   ', kkal_raskl)
        total_ygl.setdefault(day_slovar, 0)
        total_ygl[day_slovar] += ygl_raskl

        # print('== kkal ==   ', kkal_raskl)
        # total_kkal += dict_numebr_day_kort[day_slovar][product_list][0]
        # print('обращение через индекс 0   ',dict_numebr_day_kort[day_slovar][product_list][0])
        # for razdel_4_stolb in range(4):
        #     # print('I  ', razdel_4_stolb)
        #     print('index razdel 4 stolb  ', dict_numebr_day_kort[day_slovar][product_list][razdel_4_stolb])

# print(' total kkal', total_kkal, '\n', 'total belk', total_belk, '\n', 'total jir', total_jir, '\n', 'total ygl', total_ygl)
# print('словарь сложенный                                  ', dict_numebr_day_kort)


for i in range(1, 10):
    print(math.trunc(total_kkal[i]), math.trunc(total_belk[i]), math.trunc(total_jir[i]), math.trunc(total_ygl[i]))


# for i in dict_numebr_day_kort
        # for i in dict_numebr_day_kort[day_slovar][key_day_slovar]:
        #     print('== i == ',i)
    # print('== словарь со значением и == ', dict_numebr_day_kort[i])


# for numbers_day_cikl in range(1,10):
#     # print(dict_numebr_day_kort[numbers_day_cikl])
#     for name in dict_numebr_day_kort[numbers_day_cikl]:
#         print(i)



#     product_kkal = sheet_product_kkal[raskladka_name][0] * (raskladka_gram/100)
#     product_belk = sheet_product_kkal[raskladka_name][1] * (raskladka_gram/100)
#     product_jir = sheet_product_kkal[raskladka_name][2] * (raskladka_gram/100)
#     product_ygl = sheet_product_kkal[raskladka_name][3] * (raskladka_gram/100)
#     total_kkal += product_kkal
#     total_belk += product_belk
#     total_jir += product_jir
#     total_ygl += product_ygl
# print(math.trunc(total_kkal), math.trunc(total_belk), math.trunc(total_jir), math.trunc(total_ygl))
