import oracledb
import requests
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
# DB연결부분
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

year = 1

for year in range(2020,2023):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(2)
    soup  = BeautifulSoup(browser.page_source,"lxml")

# find all
container = soup.find("ul",{"class":"c-list-basic ty_flow35"})
for movies in container:
    movie_list = container.find_all("li")
    for movie in movie_list:    
        for i,movie in enumerate(movies):
            print(f"[ {i+1} 위 ]")
            # 제목
            title = movie.find("strong",{"class":"tit-g clamp-g"})
            # m_title = title.find("a")
            print("제목 : ",title.text.strip())

            # 이미지
            img_screen = movie.find("img")['src']
            print("이미지 : ",img_screen)

            # 누적관객수
            audience = movie.find("p",{"class":"conts-desc clamp-g"})
            # audi = audience.find("span",{"class":"none"}).nextSibling.strip()
            print("누적관객수 : ",audience.text.strip())
            
            #날짜
            date = movie.find("span",{"class":"conts-subdesc clamp-g"})
            # ddate = date.find("a")
            print("날짜 : ",date.text.strip().replace(",",""))
            print("-"*10)
print("종료")
            
    
#    # DB저장
#     sql = f"insert into daum_movie values (daum_movie_seq.nextval,'{title}''{img}'\
#     ,{audience},{date})"
#     cursor.execute(sql)
# print("-"*30)
# cursor.execute('commit')
# cursor.close()
# conn.close()


# 역대관객순
# 이미지, 제목,누적관객수,날짜
# 이미지 저장까지 해야 함.
# 2023,2022,2021,2020
# 콘솔창에 출력하고, db에 저장하시오.
# daum_movie 테이블
# dno 시퀀스
# title 문자타입(100)
# img 문자타입(100)
# audience 숫자타입(10)
# ddate 날짜타입

# with open(f"movie_{i}.jpg","wb") as f:
#     re_img = requests.get(img_screen) #url링크를 다시 읽어와야 함.
#     f.write(re_img.content) # 파일이름의 내용을 저장