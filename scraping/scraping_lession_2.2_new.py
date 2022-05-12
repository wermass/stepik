import pandas as pd

tabl = pd.read_excel("salaries.xlsx", index_col=0)
median_city = tabl.median(axis=1).idxmax()
median_zarplata = tabl.mean(axis=0).idxmax()
print(median_city, median_zarplata)