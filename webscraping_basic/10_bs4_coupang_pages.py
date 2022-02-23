import re
import requests
import re
from bs4 import BeautifulSoup

myheader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

for i in range(1, 6):
    print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url, headers = myheader)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    
    for item in items:
        name = item.find("div", attrs={"class":"name"}).get_text()
        # apple 제외
        if "Apple" in name:
            continue
        
        price = item.find("strong", attrs={"class":"price-value"})
        if price:
            price = price.get_text() # 출력 : (26) int로 변경해야함
        else:
            continue
            
        # 리뷰 50개 이상 평점 4.5 이상만 조회
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            continue
        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text() # 출력 : (26) int로 변경해야함
            rate_count = rate_count[1:-1]
        else:
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        
        if float(rate) >= 4.5 and int(rate_count) >= 500:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count})개")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100)