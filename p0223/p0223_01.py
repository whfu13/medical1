# 출력 print()
print('문자열') # 문자열 출력
print(10.123) # 숫자 출력
print(123*111) # 사칙연산 후 출력

# %d 정수 %f 실수 %s 문자열을 나타낸다
print("%d %f %s"%(10,12.1234,'문자'))
print("%.2f"%(22.358894)) # 소수 둘째자리까지 출력

# str.format()
print('문자열을 쓰고 {}'.format(1))
# 정수
print("{0:d}".format(123))
print('{0}'.format(123))
print("{}".format(123))
# 실수
print("{0:f}".format(123.456789))
print('{0}'.format(123.456789))
print("{}".format(123.456789))
print('{:.1f}'.format(123.456789))

# 변수
number = 10 # 정수 - int
pi = 3.14 # 실수 - float
result = True #bool - True, False
str1 = '문장입니다' # string
ch = 'A' # 문자

# 논리연산자
# and (둘이 참이어야 참) or (둘중에 하나만 참이어도 참)
# not (참=>거짓, 거짓=>참)

# 입력 받기 input()
# input()의 결과 값은 문자형

# if 조건문
# if 조건문1:
# 실행문1:
#{else:
#    실행문2}
# 조건문1이 참이면 실행문1을 실행 후 종료
# 조건문1이 거짓이면 실행문 2를 실행 후 종료