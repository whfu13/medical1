# 중첩 for
# for 안에 for
for i in range(3):
    print('안녕')
    for j in range(2):
        print('반가워')
# i = 0일떄
    # j = 0. j = 1




# for문을 사용해서 2단 출력
# 입력받은 숫자의 단을 출력하세요 >>
# 3을 입력받으면 3단출력 4를 입력받으면 4단 출력
for i in range(1,10):
    print('{}*{}={}'.format(2,i,2*i))
    
n = int(input('원하는 단을 입력하세요 >>'))
for i in range(1,10):
    print('{}*{}={}'.format(n,i,n*i))
    
for i in range(2,10): # 2단부터 9단까지 출력
    for j in range(1,10): # *1~*9
        print('{} * {} = {}'.format(i,j,i*j))

for i in range(6): # j = 0 1 2 3 4
    print('[{} 단]'.format(i))
    for j in range(1,6): # i = 1 2 3 4 5
        print('{} * {} = {}'.format(i,j,i*j),end=' ')
    print()    # 줄바꿈
print('for 끝')

# 짝수단만 출력
for i in range(2,10):
    if i % 2 == 0:
        print('[{} 단]'.format(i))
    for j in range(1,6):
            print('{} * {} = {}'.format(i,j,i*j),end=' ')
# 홀수단만 출력
for i in range(2,10):
    print('[{} 단]'.format(i))
    for j in range(1,10):
        if j % 2 == 1:
            print('{} * {} = {}'.format(i,j,i*j),end=' ')