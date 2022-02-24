import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

myheader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Accept-Language":"Ko-KR,Ko"}
url = "https://play.google.com/store/movies"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 지정한 위치로스크롤 내리기
# browser.execute_script("window,scrollTo(0, 2080)") # 해상도 2080 위치로 스크롤 내리기

# 화면 가장 아래로 스크롤 내리기


interval = 2 # 2초에 한번씩 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window,scrollTo(0, document.body.scrollHeight)") # 화면 가장 아래로 스크롤 내리기
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"})

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    
    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

    #링크 정보
    link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    
    print("제목 : ", title.text)
    print(f"할인 전 가격 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("랑크 :", "http://play.google.com" + link)
    print("*" * 120)

browser.quit()