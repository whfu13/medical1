# medical_1.csv 파일을 읽어와서 출력하시오.

# 파일 열기
f = open("medical_1.csv","r",encoding="utf8")
sum = 0
# 파일 읽기
cnt = 0
while True:
    content = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content == "":break
    c_list = content.split(",")
    print(c_list,len(c_list))
    c_list[1] = int(c_list[1])
    sum += c_list[1]
    # print(content,end="")
print("기초생활수급대상자 전체 수: ",sum)
# 파일 닫기
f.close()

# 기초생활수급자 총인원 합계
