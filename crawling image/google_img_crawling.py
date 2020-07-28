import os
import urllib.request
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

search = input('원하는 사진의 검색어를 입력해주세요 : ')
getNumber = int(input('원하는 이미지 매수를 입력해주세요 : '))
url ='https://www.google.com/search?q={}&newwindow=1&hl=ko&sxsrf=ALeKk01gKZUgYf6JNfT21Y5L6M2vXF3Anw:1595593439610&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjpzbHh8OXqAhWKad4KHThmAKcQ_AUoAXoECAwQAw&biw=1440&bih=766'.format(quote_plus(search))

driver = webdriver.Chrome('/Users/sang-woolee/Desktop/Project/kao_class/chromedriver')
driver.get(url)

#웹드라이버를 열고 스크롤을 내리는 코드
for i in range(500):
    driver.execute_script("window.scrollBy(0,10000)")

html = driver.page_source
soup =BeautifulSoup(html, 'html.parser')

img = soup.select('.rg_i.Q4LuWd')

imgurl = []

n = 1

for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])



if not os.path.exists('/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(search)):
    os.makedirs('/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(search))

print('사진을 {} 폴더에 다운로드하는 중입니다...'.format(search))
for i in imgurl:
    urlretrieve(i, '/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(search) + search + str(n) + '.jpg')
    n += 1

    if n == getNumber + 1:
        driver.close()
        print('이미지 {}장 다운로드 완료'.format(n-1))
        break


# for i in img:
#     imgUrl = i['data-source']
#     with urlopen(imgUrl) as f:
#         with open('/Users/sang-woolee/Desktop/Project/kao_class/{}/'.format(plusUrl) + plusUrl + str(n) + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)
#     n += 1

