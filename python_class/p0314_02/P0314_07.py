# str.txt 파일의 내용을 모두 출력하시오.
f = open("str.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt.strip() == "" : break
    print(txt,end="")
    
    
f.close()
    
# str.txt 파일 내용을 읽어와서
# str1.txt에 그 내용을 추가해보세요.
f = open("str.txt","r",encoding="utf8")
file = open("str1.txt","a",encoding="utf8")

while True:
    content = f.readline() # 파일내용을 읽어오기
    if content.strip() == "": break
    file.write(content) # 파일내용을 추가하기
    
f.close()
file.close()

fff = open("str1.txt","r",encoding="utf8")
while True:
    content = fff.readline()
    if content.strip() == "": break
    print(content,end="")

fff.close()