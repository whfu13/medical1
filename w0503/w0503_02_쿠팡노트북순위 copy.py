import oracledb
import random
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# DB 연결 부분
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
page = 1
for page in range(1,4):
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    time.sleep(2)
    
    soup = BeautifulSoup(browser.page_source,"lxml")

# elem = browser.find_elements(By.CLASS_NAME,"coupang-search is-speech")
# elem = browser.find_element(By.CLASS_NAME,"coupang-search is-speech ad-keyword")
# elem.send_keys("노트북")
# elem.send_keys(Keys.ENTER)
# elem.click()
# time.sleep(5)

container = soup.find("ul",{"class":"search-product-list"})
coupang = container.find_all("li")
        # print("개수 : ",len(coupang))
for i,cp in enumerate(coupang):
    print(f"[ {i+1}번째 상품 ]")
    # 제목
    title = cp.find("div",{"class":"name"}).text.strip()
    print("제목 : ",title)

    # 이미지
    img = cp.find("img",{"class":"search-product-wrap-img"})["src"]
    # 파일 저장
    with open(f"coupang_{i+1}.jpg","wb") as f:
        d_img = requests.get(img)
        f.write(d_img.content)
    print("이미지 : ",img)

    # 금액
    price = cp.find("strong",{"class":"price-value"}).text.strip()
    print("금액 : ",price)

    # 평점
    grade = cp.find("span",{"class":"star"})
    score = float(score.text)
    print("평점 : ",grade.text.strip())
    print("-"*10)

    # 평가수
    eval_num = cp.find("span",{"class":"rating-total-count"})
    eval_num = int(eval_num.text[:-4].replace(",",""))
    print("평가수 : ",eval_num)
    print("-"*10)

# 검색 - 노트북으로 해서
# 콘솔에 출력하고, db에 저장하시오.
# - coupang 테이블
# cno 시퀀스
# title 문자타입(100)
# img 문자타입(100)
# price 숫자타입(10)
# grade 숫자타입(10)
# eval_num 숫자타입(10)
# 제목, 이미지, 금액, 평점, 평가수