# 매개변수 순서 중요, 매개변수 타입도 중요

def str_print(txt,num):
    for i in range(num):
        print(txt)
        

txt = input("출력하고 싶은 글자를 입력하세요.>> ")
num = int(input("출력하고 싶은 글자 반복횟수를 입력하세요."))
str_print(txt,num)

