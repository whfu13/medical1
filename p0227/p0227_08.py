# 반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값) :
'''
for i in range(3):
    print('안녕')
    # i = 0일때
    # i = 1일때
    # i = 2일때
    
for i in range(3): # i = 0, 1, 2
    print(i) 
    
for i in range(100):
    print(i+1)
    
# 숫자 한개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요
sum100 = 0
n1 = int(input("숫자를 입력하세요 >> "))
for i in range(1,n1+1):
    sum100 += i
    
print('1부터 n1까지의 합은: {}입니다'.format(sum100))

# 짝수의 합만 구함

for i in range(1,11):
    if i % 2 == 0:
        print(i)
    
for i in range(1,n1+1):
    sum100 = sum100 + i
    
print('1부터 n1까지 짝수의 합은: {}입니다'.format(sum100))

# 1-10까지의 곱
num100 = 1
for i in range(1,11):
    num100 *= i

print('1부터 10까지의 곱은: {}입니다'.format(num100))