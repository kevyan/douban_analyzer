from bs4 import BeautifulSoup
import requests

baseUrl = 'https://movie.douban.com/subject/27615233/comments?start='
endUrl = '&limit=20'
startArr = ["1", "21", "41", "61", "81", "101"]
urlArr = []

# def getUrl():
for i in range(6):
    url = baseUrl + startArr[i] + endUrl
    urlArr.append(url)
print(urlArr)

for i in range(6):
    src = requests.get(urlArr[i]).text

    soup = BeautifulSoup(src, 'lxml')

    infolist = []

    obj = soup.find_all('span', class_='rating')
    for element in obj:
        print(element)


