import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml 파서를 통해 beatifulsoup으로 만듦
print(soup.title)
print(soup.title.get_text())
print(soup.a) # a 엘리먼트에 대한 내용을 print함