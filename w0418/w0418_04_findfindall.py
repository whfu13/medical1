import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 태그로 찾는 방법 title, get_text(), text, a.attrs, a["href"]
# find : 태그정보 찾기 함수
#  class로 찾는 방법
# print(soup.find(attrs={"class":"box_type_l"}))
# print(soup.tr)
print(soup.find("tr",attrs={"class":"type1"})) #find, find_all, class
type_tr = soup.find("tr",{"class":"type1"})
print("th : ",type_tr.th) # 1번째 만나는 th태그를 찾아줌.
print(type_tr.find_all("th")) # 모든 th태그 찾아줌.
ths = type_tr.find_all("th")
for th in ths:
    print("제목 : ",th.text)