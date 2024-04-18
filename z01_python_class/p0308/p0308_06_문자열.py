# 인덱싱[0],슬라이싱[0:4][:3][1:],len,upper,lower,swapcase,title

shape_list = ["spadE","diamonD","heart","clover"]
for i in shape_list:
    print(i.upper())# 대문자 출력
    print(i.title())
    print(i.swapcase())
    print(i.lower()) # 소문자 출력
# title = "안녕하세요"
# # 역순출력 => 요세하녕안
# for i in range(len(title)):
#     print(title[(len(title)-1)-i],end="")
# a = [1234,11111,1,145,20,1323456547]
# # 리스트의 각 숫자의 길이를 출력
# # 짝수만 문자길이를 출력
# for i in a:
#     if i%2 == 0:
#         print("숫자:{}, 길이:{} ".format(i,len(str(i))))
        
# # 한글자씩 출력을 해보세요
# title = "혼자공부하는파이썬수업"
# for i in range(len(title)):
#     print(title[i])
    
# a = input("문자를 입력하세요.")
# print("현재 입력한 문자 길이 : ",len(a))

# a = 100000
# b = "안녕하세요.반갑습니다.저는 홍길동입니다"
# print(len(str(a)))
# print(len(b)) # 문자열 길이
# print(b[0])
# print(b[2])
# print(b[2:5])


# a = "안녕"
# b = 1
# c = 2
# d = "10"
# print(b+c)
# print(b+int(d))