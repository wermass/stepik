
from urllib.request import urlopen
from bs4 import BeautifulSoup


#url = 'https://stepik.org/media/attachments/lesson/209723/3.html'


#response = request.get(url)

#soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf-8')  #  открыл юрл, почему то только ссылку с сайта, если качаю со степика, открыть не получается file:///C:/msys64/home/User/stepik/scraping/3.html
s = str(html)  #  делаем html строкой(ток за чем?)
soup = BeautifulSoup(s, 'html.parser')  #  magic
no_teg = soup.find_all('td')  #  находим все значения в теге
numbers_lists = []  #  список для значений, будет заноситься из цикла
numbers_sum = 0  #  сумма чисел
for i in no_teg:  #  цикл, заносит значения в список
    numbers = i.get_text()
    #print(numbers)
    numbers_lists.append(numbers)
 
for i in numbers_lists:
    numbers_int = int(i)
    numbers_sum += numbers_int
print(numbers_sum)
