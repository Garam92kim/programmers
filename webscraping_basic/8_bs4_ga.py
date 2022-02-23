import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("http://comic.naver.com" + link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "http://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

#평점 정보 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 : ", total_rates, "평균 :", total_rates / len(cartoons))

# 터미널에서 python 입력 후 한줄씩 입력해서 결과를 확인 할 수도 있음
# beautifulsoup 한글 문서도 있음