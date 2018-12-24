from bs4 import BeautifulSoup
import requests

src = requests.get('https://movie.douban.com/subject/27615233/').text

soup = BeautifulSoup(src, 'lxml')

infolist = []

for div in soup.find_all('div', class_='info'):
    infolist.append(div.prettify())
    print(infolist)
    