import pandas as pd
import math


dicts = []

for numbers_xlsx in range(1, 1001):
    vedomostb = pd.read_excel(f'C:/msys64\/home/User/stepik/scraping/Pycharm/firsts/rogaikopyta/{numbers_xlsx}.xlsx')
    vedomostb.fillna(0, inplace=True)
    # print('vedomostb iterrows     ', vedomostb.iterrows())
    for product_row in vedomostb.iterrows():
        a = product_row[1][1], product_row[1][3]
        dicts.append(a)
for i in range(1, 1001):
    dicts.remove(('ООО "Рога и копыта"', 0.0))

for i in range(1000):
    b = sorted(dicts)
    print(b[i][0], int(b[i][1]))
# print(sorted(dicts))
# print(dicts)






#         # print(a[0])
#         # print(type(a))
#         # for i in a:
#         #     print(i)
# #         a = dicts.setdefault(product_row[1][1], product_row[1][3])
# #         # print(a, '    end     ')
# dicts.pop('ООО "Рога и копыта"')
# a = sorted(dicts)
# # print(a)
# dicts1 = {}
# for i in a:
#     dicts1.setdefault(i, int(dicts[i]))
# for i in dicts1:
#     print(i, dicts1[i])
