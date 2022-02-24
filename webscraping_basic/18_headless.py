import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

web_option = webdriver.ChromeOptions()
web_option.headless = True
web_option.add_argument("window-size=2560x1440")
web_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser = webdriver.Chrome(options=web_option)
browser.get(url)

myagent = browser.find_element_by_id("detected_value")
print(myagent.text)
browser.quit()

# google - selenium with Python 공부

# interval = 2 # 2초에 한번씩 스크롤 내리기
# prev_height = browser.execute_script("return document.body.scrollHeight")

# while True:
#     browser.execute_script("window,scrollTo(0, document.body.scrollHeight)") # 화면 가장 아래로 스크롤 내리기
#     time.sleep(interval)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
    
#     if curr_height == prev_height:
#         break
    
#     prev_height = curr_height

# print("스크롤 완료")
# browser.get_screenshot_as_file("google_movie.png")

# soup = BeautifulSoup(browser.page_source, "lxml")
# movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
# print(len(movies))

# for movie in movies:
#     title = movie.find("div", attrs={"class":"Epkrse"})

#     # 할인 전 가격
#     original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
#     if original_price:
#         original_price = original_price.get_text()
#     else:
#         continue
    
#     # 할인 된 가격
#     price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

#     #링크 정보
#     link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    
#     print(f"제목 : {title}")
#     print(f"할인 전 가격 : {original_price}")
#     print(f"할인 후 금액 : {price}")
#     print("랑크 :", "http://play.google.com" + link)
#     print("*" * 120)

# browser.quit()