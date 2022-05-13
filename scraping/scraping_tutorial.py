import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
img = tonight.find("img")
desc = img['title']
period_tags = seven_day.select(".tombstone-container .period-name")  # здесь и далее, что такое seven_day.select
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]  # tyt
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]  # tyt
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]  # and tyt
weather = pd.DataFrame({             # почему он вывел не все колонки как на сайте? (cs_1 pycharm sc_2 сайт)
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
#print(weather)

# код от сих с ошибкой
temp_nums = weather["temp"].str.extract("(?Pd+)", expand=False)  # копировал с сайта и тут ошибка, сам не смог понять по чему, sc_3
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)
# до сих

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
#print(is_night)