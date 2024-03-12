# 해보세요
# 1. 나이가 10살 이상이고 150 이상만 탑승가능
# 나이, 키를 입력받아
# [탑승가능] [탑승불가능]을 출력해보세요

# 2. 숫자 3개 (정수)를 입력받고, 연산1개를 입력받아
# +++ --- *** /// (나누기값은 둘째자리까지 표현)
# a + b + c = d의 형태로 출력 (1 + 2 + 3 = 6)
age = 11
height = 130

age = int(input("나이를 입력해주세요 >> "))
height = int(input("키를 입력해주세요 >> "))

if age >= 10 and height >= 150:
    print("놀이기구 탑승 가능")
else:
    print("놀이기구 탑승 불가능")   
    
cal= input("수식을 입력해주세요 >> ")
n1= int(input("첫번째 숫자를 입력해주세요 >> "))
n2= int(input("두번째 숫자를 입력해주세요 >> "))
n3= int(input("세번째 숫자를 입력해주세요 >> "))

if cal == "+":
    print("{}+{}+{}= {}".format(n1,n2,n3,n1+n2+n3))
elif cal == "-":
    print("{}-{}-{}= {}".format(n1,n2,n3,n1-n2-n3))
elif cal == "*":
    print("{}*{}*{}= {}".format(n1,n2,n3,n1*n2*n3))
elif cal == "/":
    print("{}/{}/{}= {}".format(n1,n2,n3,n1/n2/n3))
else:
    print('잘못입력하셨습니다.')                
    
    
if cal == '+':
    result = n1 + n2 + n3
elif cal == '-':
    result = n1 - n2 - n3
elif cal == '*':
    result = n1 * n2 * n3
elif cal == '/':
    result = n1 / n2 / n3
else:
    print('잘못입력하셨습니다.')                