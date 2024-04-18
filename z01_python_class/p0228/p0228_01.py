n = 10 # int(input('숫자를 입력해주세요 >> '))
if n >= 0 :
    print('양수')
    if n%2 == 0:
        print('짝수')
    else:
        print('홀수')    
else:
    print('음수')    
    
'''
반복문
for 변수 in 반복가능한데이터:
    실행문

'''

# 순차적으로 커질때는 range를 사용한다.
for i in range(0,3,1): # range(시작값, 끝값+1, 증감값)
    print('hi')        # i가    0       2+1     1
    # i = 0일때, hi
    # i = 1일때, hi
    # i = 2일때, hi
    
for i in range(5): # i가 0부터 4까지 반복해라 > 5번 반복해라
    print(i)
    
for i in range(1,11):
    print(i)
    
a = 10
b = '안녕하세요'
# a,b를 5번 반복해서 출력
for i in range(5): # i는 0-4
    print(i)
    a = a + 1
    print(a)
    print(b)
    
# i = 0 , i = 0 , 10 + 1 => 11
# i = 1 , i = 1 , 11 + 1 => 12

# 입력 : 이름, 점수 (5명의 이름과 점수를 입력받습니다)
# 60점 이상이면 합격, 60점 미만이면 불합격을 출력하는데
# 출력의 형태는 [홍길동님 합격입니다] [홍길동님 불합격입니다]



for i in range(5):
    name = input('이름을 입력하세요 >> ')
    score = int(input('점수를 입력하세요 >> '))
    if score >= 60 :
        print('{}님 합격입니다'.format(name))
    else:
        print('{}님 불합격입니다'.format(name)) 