import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# selenium으로 정보 가져오기
browser = webdriver.Chrome()
url = "https://comic.naver.com/bestChallenge"
browser.get(url)

# 페이지로딩시간을 최대한 보장
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
best = soup.find("ul",{"class","AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
lis = best.find_all("li")

for li in lis:
    title = li.find("span","ContentTitle__title--e3qXt").text
    img_url = li.find("img")['src']
    print("순위 : ",li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
    print("제목 : ",title)
    print("작가 : ",li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
    print("이미지링크 : ",img_url)
    img_poster = requests.get(img_url,headers=headers)
    #이미지파일 저장방법
    
    with open("{}.jpeg".format(title),"wb") as f:
        f.write(img_poster.content)
    print("-"*40)
    

    

# with open("webtoons2.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

# requests 정보 가져오기
# url ="https://comic.naver.com/bestChallenge"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())
# with open("webtoons1.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())
# print("완료")