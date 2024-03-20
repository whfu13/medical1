# input 입력받은 데이터를 
# p_0320.txt 파일을 생성해서 저장하시오.
# p_0320은 현재날짜를 사용하시오.
import datetime

now = datetime.datetime.now()
print(now.month)
print(now.day)
print(now.strftime("%m%d"))
fileName = "p_"+ now.strftime("%m%d") + ".txt"
d = input("내용을 입력하세요 >>")
with open(fileName,"w",encoding="utf8") as f:
    f.write(d+"\n")
f.close()
