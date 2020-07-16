# /Applications/Chrome.app
from urllib.request import urlopen
from bs4 import BeautifulSoup

html  = urlopen('http://www.naver.com')
bsObject = BeautifulSoup(html, 'html.parser')

print(bsObject)