from email import header
import requests

url = "http://nadocoding.tistory.com" # 접속 url
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
res = requests.get(url, headers=header)
res.raise_for_status() #오류시 프로그램 종료시킴

# user agent string, what is my user agent?

with open("nadocoding.html", 'w', encoding="utf8") as f:
    f.write(res.text)