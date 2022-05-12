import xlrd
from statistics import mean


rb = xlrd.open_workbook('salaries.xlsx')
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)[1]
slovar = {}
#sum1 = 0
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
for j in vals[1:]:  #  создал словарь с ключами городов и переменными значений
    slovar.setdefault(j[0], [])
    #print(j, 'j')
    #print(slovar[j[0]], 'slovar[j[0]]')
    for k in range(1, len(vals)-1):
        w = int(j[k])

        slovar[j[0]].append(w)
#print(slovar)
means_end = []
for city in slovar:
    #print(city)
    means = []
    #print(slovar[city])

    for numbers in range(len(slovar)-1):
        chisla_iz_spiska = slovar[city][numbers]
        means.append(chisla_iz_spiska)
        #print(chisla_iz_spiska)
#print(slovar)
proffesion = []

for j in vals[:][0]:
    proffesion.append(j)
    #print(j)
proffesion_1 = proffesion[1:]
proffesion_slovar = {}
subject = vals[1][1:]
for i in proffesion_1:
    proffesion_slovar.setdefault(i, [])

#print(proffesion_slovar, 'proffesion_slovar')
b = 1
for j in proffesion_slovar:
    #print(j, 'j')
    for i in range(1,9):
        #print(i, 'i')
        a = int(sheet.row_values(i)[b])
        proffesion_slovar[j].append(a)
        #print(a, 'a')
    b += 1
        #lovar[j[0]].append(w)

print(proffesion_slovar, 'proffesion_slovar')
for i in proffesion_slovar.values():
    print(sum(i)/8)