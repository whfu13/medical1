import oracledb
import requests
import time
import random
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

url = f"https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source,"lxml")
###. find_all
melons = soup.find_all("tr",{"id":"lst50"})
melons += soup.find_all("tr",{"id":"lst100"})
print("전체 개수 : ",len(melons))
for i,melon in enumerate(melons):
    print(f"[ {i+1} 위 ]")
    # 1. 순위
    rank = melon.find("span",{"class":"rank"})
    print("순위 : ",rank.text.strip())
    # 2. 순위 변동
    m_rank = melon.find("span",{"class":"rank_wrap"})
    v_rank = melon.find("span",{"class":"rank_wrap"})['title']
    if v_rank == '순위 동일':
        v_rank = 0
    elif v_rank.find('단계 하락') != -1:
        v_rank = m_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    else:
        v_rank = m_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)
    print("순위 변동 :{:+d} ".format(v_rank)) # +부호 넣기
    # 3. 이미지
    img = melon.find("img")['src']
    print("이미지 : ",img)
    # 4. 제목
    title = melon.find("div",{"class":"ellipsis rank01"})
    m_title = title.find("a")
    print("제목 : ",title.text.strip())
    # 5. 가수
    singer = melon.find("div",{"class":"ellipsis rank02"})
    r_singer = singer.find("a")
    print("가수 : ",singer.text.strip())
    # 6. 좋아요수
    likeNum = melon.find("button",{"class":"button_etc like"})
    r_likeNum = likeNum.find("span",{"class":"none"}).nextSibling.strip()
    # price = int(likeNum.text.replace(",",""))
    print("좋아요수 : ",r_likeNum)
    print("-"*10)
#     # DB저장
#     sql = f"insert into yeogi values (melon_seq.nextval,{rank},{v_rank}\
#     ,'{img}','{title}','{singer}',{likeNum})"
#     cursor.execute(sql)
# print("-"*30)
# cursor.execute('commit')
# cursor.close()
# conn.close()
# find,find_all

# # 파일저장
# with open("melon.html","w",encoding="utf-8")as f:
#     f.write(soup.prettify())
    
# # 파일 불러오기
# with open("melon.html","r",encoding="utf-8")as f:
#     soup = BeautifulSoup(f,"lxml")