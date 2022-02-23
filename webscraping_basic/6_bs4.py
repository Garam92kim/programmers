import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml 파서를 통해 beatifulsoup으로 만듦
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # a 엘리먼트에 대한 내용을 출력
# print(soup.a.attrs) # a 엘리먼트의 속성을 출력
# print(soup.a["href"]) # 대괄호 안의 속성값 정보를 출력

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 클래스값이 Nbtn_upload 인 a element를 찾아줘
 # a 가 없으면 Nbtn_upload 인 element를 찾아줌
 
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank1 기준으로 앞뒤로 움직여봄

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rankd2.a.get_text)

# print(rank1.find_next_siblings("li")) # sibling 과 달리 모두 가져옴

webtoon = soup.find("a", text="튜토리얼 탑의 고인물-96화")
print(webtoon)