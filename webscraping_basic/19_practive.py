import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

myheader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

def create_soup(url):
    res = requests.get(url, headers = myheader)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def wather_check():
    print("오늘의 날씨")
    soup = create_soup("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8")
    cast = soup.find("span", attrs={"class":"temperature up"}).get_text()
    curr_temp = soup.find("span", attrs={"class":"blind"}).get_text()
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    morning_rain_rate = soup.findAll("span", attrs={"class":"rainfall"})[0].get_text()
    afternoon_rain_rate = soup.findAll("span", attrs={"class":"rainfall"})[1].get_text()
    print(cast)
    print("현재 {} 최저{} / 최고{}".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    dust = soup.find("ul", attrs={"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text()
    pm25 = dust.find_all("li")[1].get_text()
    # pm35 = dust.find_all("li")[2].get_text()
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    # print("자외선 {}".format(pm35))
    print()

def headline_news():
    soup = create_soup("https://news.naver.com/")
    headlind = soup.find("ul", attrs={"class":"native_scroll_list cjs_headline_list"}).find_all("li", limit = 3) # class가 저거인 거에서 li를 모두 찾아 반환
    # limit 을 통해 최대 3개까지만 가져올수 있음
    for index, news in enumerate(headlind): # index 표시를 위해 index, 넣음 (1, 2, 3 ...)
        title = news.find("div").get_text().strip()
        link = "https://news.naver.com" + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크 : {}".format(link))
        print()

def scrape_it_news():
    soup = create_soup("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")
    print("[IT NEWS]")
    news_list = soup.find("div", attrs={"class":"_persist"}).find_all("ul")
    for index, news in enumerate(news_list):
        title = news.find("div", attrs={"class":"cluster_text_lede"}).get_text().strip()
        link = news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크 : {}".format(link))
        
def english_comm():
    soup = create_soup("https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english")
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    # id ^표시, re.compile로 정규식 사용 가능 (이걸로 시작하는 어떤 값을 가져옴)
    print("영어 지문")
    for sentece in sentences[len(sentences)//2:]: # 8문장이라고 가정 시 5~8까지 짤라서 가져옴 (영어지문) slicing 사용
        # 2로 나눈거부터 끝까지 진행 (4부터 끝까지)
        print(sentece.get_text().strip())
    
    print("한글 지문")
    for sentece in sentences[:len(sentences)//2]:
        print(sentece.get_text().strip())
        

wather_check()
headline_news()
scrape_it_news()
english_comm()