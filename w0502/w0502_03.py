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
browser = webdriver.Chrome()
browser.maximize_window()

url = f"https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=EAIaIQobChMIstLNpr3uhQMVStAWBR2lIg4bEAAYASAAEgL6Z_D_BwE"
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,"lxml")

# 검색창에 호텔 입력
# 사용자에게 검색어 입력
#--------------------------------------
elem = browser.find_elements(By.CLASS_NAME,'HomeSearchBar_searchBoxArea__1P61S')
elem[0].click()
time.sleep(1)
# browser.switch_to.window(browser.window_handles[1])
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[@class="NavFilterButton_container__20Hr2 NavFilterButton_collapse__3JGvV SearchInput_calendarButton__3sNMZ"]')
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]')
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[5]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
elem.send_keys('호텔')
elem.send_keys(Keys.ENTER)
time.sleep(5)
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)
cnt = 0
while True:
    if cnt == 5: break
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print('현재 높이 :',curr_height)
    cnt += 1



# 1. 야놀자 홈페이지 이동
# 2. 검색창에 호텔 입력
# 3. 날짜 선택
# 4. 6월 5일,6일 클릭
# 5. 확인 버튼 클릭
# 6. 검색창 클릭 => enter키 입력
# 7. 검색 진행
# 8. 스크롤 이동 반복
# 9. 정보창이 띄워지면 이미지,제목,평점,평가수,금액 저장
# yanolja 테이블
# yno,img,title,grade,grade_num,price