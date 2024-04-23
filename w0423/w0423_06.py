import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

url = ("https://jumin.mois.go.kr/ageStatMonth.do")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천직할시, 경기도 3개의 인구를 웹스크래핑해서
# 서울특별시 : 인구
# 인천직할시 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오.
# print(soup.find("div",{"class":"tab_section current_table title_table_div"}))
# print(soup.find("div",{"id":"content_wrap"}))
it = soup.find("div",{"class":"tab_section current_table title_table_div"})
# print("개수 : ",len(it))
items = it.find_all("tr")
# pop = soup.find("tr",{"class":"th1"})
# pop1 = pop.find_all("tr")
for i,item in enumerate(items):
    stock = items[i]
    td_list = stock.find_all("td")
    if len(td_list)<=1: continue
    print("서울특별시 : ",td_list[2].text)
    print("인천광역시 : ",td_list[5].text)
    print("경기도 : ",td_list[10].text)
    print("-"*40)
    # print("합계 : {}+{}+{}={}".format(items[4].text,items[7].text,items[12].text))