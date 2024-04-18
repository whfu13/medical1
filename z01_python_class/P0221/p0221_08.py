print("a는 %s입니다"%"입력값")
a = "입력값"
print("a는 %s입니다"%a)

# 입력함수 : input() => 문자열로 입력받는다.
a = input()
print("a는 %s입니다"%a)
a = input
print("a는 %s입니다"%a)

n1 = input
n2 = input
print("두 수의 합 : ", n1+n2)
#문자를 숫자(정수)로 바꿔준다
print("두 수의 합 (int 형): ", int(n1)+int(n2))
#문자를 숫자(실수)로 바꿔준다
print("두 수의 합 (float 형) : ", float(n1)+float(n2))

# 강제 형변환
# int 정수형
# front 실수형

a = 10 # 숫자
b = "10" # 문자
c = 20 # 숫자
d = "20" # 문자
print("숫자일때 :", a+c)
print("문자일때 :", b+d)


