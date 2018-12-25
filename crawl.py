from bs4 import BeautifulSoup
import requests

baseUrl = 'https://movie.douban.com/subject/27615233/comments?start='
endUrl = '&limit=50'

startArr = []
# startArr = ["1", "21", "41", "61", "81", "101"]
for i in range(2):
    start = 1 + (i * 50)
    startArr.append(str(start))

urlArr = []

# def getUrl():
for i in range(len(startArr)):
    url = baseUrl + startArr[i] + endUrl
    urlArr.append(url)
print(urlArr)

for i in range(len(startArr)):
    src = requests.get(urlArr[i]).text
    soup = BeautifulSoup(src, 'lxml')
    # infolist = []

    obj = soup.find_all('span', class_='rating')
    for element in obj:
        print(element)


