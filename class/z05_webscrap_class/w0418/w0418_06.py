import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("table",{"class":"type_5"}))
t_table = soup.find("table",{"class":"type_5"})
trs = t_table.find_all("tr")
tds = trs[2].find_all("td")
for td in tds:
    print(td.text.strip())
# print("<a>[1개속성] : ",soup.a["href"]) #태그의 1개 속성 가져옴.
# print(type_td.find_all("td"))
# td2 = type_td.find_all("td")
# for td in td2:
#     print("제목 : ",td.text)
