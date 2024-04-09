import os

# 파일생성(1)
f = open("students.txt","w",encoding="utf-8") 
f.write("1,'홍길동',90,100,99,289,99.97,1\n")
f.write("2,'유관순',98,93,87,278,92.67,3")

f.close() # 파일닫기

# # 파일생성(2) with 사용하면 f.close() 사용하지 않아도 됨.
# with open("students.txt","w") as f:
#     f.write("1,'홍길동',90,100,99,289,99.97,1")
    
# 파일읽어오기
t_list = []
out_f = open("students.txt","r",encoding="utf-8")
while True:
    txt = out_f.readline() # 1줄씩 읽어오기
    # print(type(txt))
    if txt == "":
        break
    print(txt,end="")
    t_list.append(txt)
print()
print(t_list)

out_f.close()
# 파일삭제
os.remove("students.txt")




# 폴더가 존재하는지 확인
# if not os.path.exists("hello"):
#     os.mkdir("hello")
# else:
#     os.rmdir("hello")