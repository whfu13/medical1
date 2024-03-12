# 변수사용
# 변수 bool, int, float, str 형이 있다.
# 변수는 대소문자를 구분한다.(대문자는 주로 클래스에서 사용)
myVar = 10
MyVar = 20
# 변수는 언더바를 포함 할 수 있고 숫자로 시작하면 안된다.
number1 = 10
my_number = 20

# 변수는 예약어를 사용할 수 없다
# if = 100
# True = 100

# 변수는 마지막으로 입력된 값을 저장한다.
a = 10
a = 30

print(a)

a = 1
b = 2
c = 3
print(1+2+3)
print(a+b+c)

var2 = 200
var1 = var2 + 100
print(var1, var2)

a = 1
b = 2
a, b = 1, 2

# 입력 받기
# input()      : 입력을 받는 함수

# name = input("이름을 입력하세요 : ")
print('당신의 이름은 '+name+'입니다')

# input()은 문자열로 입력이 된다.

# age = input("나이를 입력하세요 : ")

# 숫자로 바꿔주기
# 1. age = int(input("나이를 입력하세요 : "))
# 2. age = int(age)
# 3.

print('당신은 내년에 {}살입니다'.format(int(age)+1))

# 숫자 하나를 입력받아서 구구단(~3까지)을 출력해보세요
# 2를 입력 받으면
# 출력:
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6

num = 2

num1 = input("구구단을 입력하세요 : ")
print('구구단 2*1= {}입니다'.format(int(num)*2))
