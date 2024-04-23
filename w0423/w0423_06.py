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
print(soup.find("div",{"class":"tab_section current_table title_table_div"}))
item = soup.find("div",{"class":"tab_section current_table title_table_div"})
items = item.find("table",{"class":"tbl_type1"})
print("서울특별시 : ",soup.find("td",{"class":"td_admin th1"}).text)
print("시 : ",soup.find())
print("서울특별시 : ",soup.find())