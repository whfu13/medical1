import requests

# 웹 스크래핑
# res = requests.get("https://www.google.com/")
res = requests.get("https://www.naver.com/")
res.raise_for_status() # 에러코드이면 자동 멈춤
print(type(res.text))
print("총 문자 길이 :", len(res.text))

with open("google.html","w",encoding="utf8") as f:
    f.write(res.text)