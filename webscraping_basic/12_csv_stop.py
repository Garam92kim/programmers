import csv
from bs4 import BeautifulSoup
import requests

myheader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # excel에서 한글 깨지면 encoding 저렇게 바꾸기
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# [string 형태의 list로 들어감]
writer.writerow(title)


for page in range(1, 2):
    res = requests.get(url + str(page), headers = myheader)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미없는 data skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)