import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup)

# 1개 best상품 출력
type_best = soup.find("div",{"class":"best-list"})
print("순위 : ",soup.p.text)
print("제목 : ",soup.find("a",{"class":"itemname"}).text)
print("가격 : ",soup.find("div",{"class":"s-price"}).strong.span.text)

# 여러개 best 상품 출력
type_li = type_best.findAll("li")
print("베스트 상품 개수 : ",len(type_li))
for li in type_li[0:4]:
    print("순위 : ",li.p.text)
    print("제목 : ",li.find("a",{"class":"itemname"}).text)
    print("가격 : ",li.find("div",{"class":"s-price"}).strong.span.text)
    print(li.text.strip())
    print("-"*30)