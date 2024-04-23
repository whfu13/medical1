import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium은 자동화프로그램
# browser = webdriver.Chrome()
# url = ("https://news.naver.com/main/ranking/popularDay.naver")
# # 브라우저 페이지 열기
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,"lxml")


url = ("https://news.naver.com/main/ranking/popularDay.naver")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
item = soup.find("div",{"class":"_officeCard _officeCard0"})
ranks = item.find_all("div",{"class":"rankingnews_box"})
print("개수 : ",len(ranks)) # 12개
print("순위 : ",soup.find("em",{"class":"list_ranking_num"}))
print("제목 : ",soup.find("a",{"class":"list_title"}))
print("이미지 링크 : ",soup.find("a",{"class":"list_img nclicks('RBP.rnknws')"}))

for rank in ranks:
    items = rank.find_all("li")
    print("제목 : ",soup.find("a",{"class":"list_title"}).text)
    print("li 개수 : ",len(items))
    print("-"*40)