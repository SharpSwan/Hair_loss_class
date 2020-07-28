import os
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
# from selenium import webdriver

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

# driver = webdriver.Chrome('/Users/sang-woolee/Desktop/Project/kao_class/chromedriver')
# driver.get(url)
#
# #웹드라이버를 열고 스크롤을 내리는 코드
# for i in range(500):
#     driver.execute_script("window.scrollBy(0,10000)")


print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

print(img[0])

if not os.path.exists('/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(plusUrl)):
    os.makedirs('/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(plusUrl))

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(plusUrl) + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1

print('다운로드 완료')