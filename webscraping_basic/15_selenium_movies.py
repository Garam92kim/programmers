import requests
from bs4 import BeautifulSoup
myheader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Accept-Language":"Ko-KR,Ko"}
url = "https://play.google.com/store/movies?hl=ko&gl=US"
res = requests.get(url, headers=myheader)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"WHE7ib mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify()) # heml 이쁘게? 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)