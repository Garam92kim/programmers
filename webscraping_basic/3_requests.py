import requests
res = requests.get("http://google.com")
res.raise_for_status() #오류시 프로그램 종료시킴

print(len(res.text))
print(res.text)

with open("mygoogl.html", 'w', encoding="utf8") as f:
    f.write(res.text)