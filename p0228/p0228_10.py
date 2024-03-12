# n1단부터 n2단까지 출력하세요
# n1 = input('숫자입력')
# n2 = input('숫자입력')

# 크기 비교해서 n1더 크면 n2.n1값 바꾸기
# 출력 2, 4  
# # 2단부터 4단까지 출력

n1 = int(input('첫번째 숫자를 입력하세요 >> '))
n2 = int(input('두번째 숫자를 입력하세요 >> '))
for i in range(n1,n2+1): # 2단
    for j in range(1,10): # *1 ~ *9
        print('{} * {} = {}'.format(i,j,i*j),end= '\t')
    
for i in range(2,5):
    for j in range(n1,n2+1):
            print('{} * {} = {}'.format(i,j,i*j),end='\t')