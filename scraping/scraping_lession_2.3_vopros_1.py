#  https://stepik.org/lesson/245290/step/2?unit=217516  урок

import pandas as pd

df = pd.ExcelFile("trekking1.xlsx").parse()
df_sorted = df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])  #  magic

# print(df_sorted['Unnamed: 0'])

for i in df_sorted['Unnamed: 0']:
    print(i)  #  что бы вывести названия без помех и записать в урок