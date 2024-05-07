import pandas as pd
# data = {
#     'year':['2019','2020','2021','2022','2023'],
#     'title':['극한직업','남산의 부장들','모가디슈','범죄도시2','서울의봄'],
#     'viewer':[1626,475,361,1269,1312],
#     'rating':['3.6','3.5','3.6','3.5','4.1']
# }
import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

m_dict = {}
year_list = []
title_list = []
viewer_list = []
rating_list = []

for year in range(2019,2024):
    print("년도 : ",year)
    year_list.append(year)
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(2)

    soup = BeautifulSoup(browser.page_source,"lxml")
    basic_list = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    
    movie_list = basic_list.find_all("li")
    print(len(movie_list))
    for i,movie in enumerate(movie_list[0]):
        # 제목
        d_strong = movie.find("strong",{"class":"tit-g clamp-g"})
        title = d_strong.find("a").text.strip()
        print("제목 : ",title)
        title_list.append(title)
        
        # 관객수
        d_audience = movie.find("p",{"class":"conts-desc clamp-g"})
        viewer = int(d_audience.find("a").text.strip()[3:-2].replace(",",""))
        print("관객수 : ",viewer)
        viewer_list.append(viewer)
        
        # 영화 평점 클릭
        elem = browser.find_element(By.XPATH,'//strong[@class="tit-g clamp-g"]')
        time.sleep(1)
        time.sleep(1)
        elem.click()
        
        # 평점
        rating = browser.find_element(By.CLASS_NAME,'gem-star-point')
        rating = float(rating.text[2:5])
        print("평점 : ",rating)
        rating_list.append(rating)
        browser.back()
        print("-"*50)
        
        
print("종료")

# dict저장
movie_list['year'] = year_list
movie_list['title'] = title_list
movie_list['viewer'] = viewer_list
movie_list['rating'] = rating_list
print(movie_list)
df = pd.DataFrame(movie_list)
print(df)