'''
for 변수 in 반복가능데이터 :
    수행문장
    
for 변수(요소) in 리스트명 :
    반복하고싶은실행문
for i in range(시작값, 끝값+1, 증감값):
    반복하고싶은 실행문
>> 실행문이 i가 시작값부터 끝값까지 반복

for i in range(반복수1):
    실행문1
    for j in range(반복수2):
        실행문2
        
>> 실행문1이 반복수1만큼 반복
>> 실행문2는 반복수1*반복수2 반복

'''
for i in range(5) : # 5번 반복 i = 0,1,2,3,4
    print('i = ', i)
    print('-'*25)
    for j in range(3): # 3번 반복 j = 0 1 2
        print('j =', j)
        
# 구구단
# 2단 출력
for i in range(1,10):
    print('{}*{}={}'.format(2,i,2*i))
    
# 구구단 전체 출력
for i in range(2,10): # i = 2-9단
    print('{}단'.format(i))
    for j in range(1,10): # 1 ~ *9
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()