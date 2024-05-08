# 반복문 for문 while문
'''
for i in range(시작,끝+1,증감값):
    수행할문장
    
while 조건식:
    실행할 문장
    
변수 = 시작값 # ex ) i = 0
while 변수 < 끝값: # 이조건이 참일때
    반복구문
    변수 = 변수 + 증가값 # i = i + 1
'''

# for 문으로 안녕하세요를 3번 출력

for i in range(3):
    print('for : 안녕하세요')
    
# while문으로 작성
i = 0
while i < 3:
    print('while : 안녕하세요')
    i += 1
    
# for문으로 0 - 10까지 출력
for i in range(0,11):
    print(i, end =' ')
# while문으로도 0 - 10까지 출력
i = 0
while i < 11:
    print(i)
    i = i + 1
    
# while을 사용해서
# 해보세요
# 1 - 10 사이의 3의 배수를 출력해보세요: 3,6,9
j = 0
while j < 11:
    if j % 3 == 0:
        print(j, end= ' ')
        j += 1
# 1 - 100 사이의 홀수를 출력
j = 1
while j < 101:
    if j%2 == 1:
        print(j ,end ='\t')
    j += 1
# 1 - 100 까지의 합을 구해보세요
sum100 = 0
j = 1
while j < 101:
    sum100 += j
    j += 1
print(sum100)

# while True: # 무한히 반복시키고자 할때 사용
#     print('ㅋ',end=' ')
# while 조건문이 참인경우 반복
# 무한루프에 들어가면 컨트롤+c를 눌러서 강제종료 할 수 있다.
# while문을 사용할때 조건문을 잘 만드는게 중요하다.

# break, continue
# break 반복문을 빠져나와서 다음단계를 수행한다.
n = 0
while n<100:
    print(n, end=' ')
    if n == 4:
        break
    n = n + 1
    
breakletter = input('중단할 문자를 입력하세요 >> ')
for letter in 'python' :
    if letter == breakletter:
        break
    print(letter)
    
while True:
    n = input('숫자를 입력해주세요(종료:0)')
    print(n)
    if n == '0':
        print('종료되었습니다')
        break
print('프로그램이 종료되었습니다')