import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time

url = "https://realty.daum.net/home/officetel/items?lat_south=37.5360221862793&lat_north=37.5360221862793&lng_west=126.63097381591797&lng_east=126.63097381591797&need_more_zoom_in=false"

web_option = webdriver.ChromeOptions()
web_option.headless = True
web_option.add_argument("window-size=2560x1440")
web_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")


browser = webdriver.Chrome(options=web_option)
browser.get(url)
browser.maximize_window()
# res = requests.get(url, headers = myheader)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# soup = BeautifulSoup(browser.page_source, "lxml")

# 하기전에 우선 html 파일로 열어봐서 원하는 정보가 있는지 확인해보기 중요!
# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button")

myagent = browser.find_element_by_xpath("//*[@id='link_home2']")
print(myagent.text)