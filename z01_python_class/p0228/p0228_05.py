# n1부터 n2까지의 합

n1 = int(input('첫번째 숫자를 입력하세요 >> '))
n2 = int(input('두번째 숫자를 입력하세요 >> '))

n100 = 0

# n1, n2 비교해서 작은수를 n1에 넣기
if n1 > n2: # n1,n2를 비교해서 n1이 작을경우
    n1,n2 = n2,n1 # n2의 값과 n1의 값을 서로 바꿔줌
    
    
for i in range(n1,n2+1):
    n100 += i

print("n1+n2는 {}입니다".format(n100))

odd_list = [] # n1-n2까지의 홀수 값을 저장

for i in range(n1,n2+1):
    if i % 2 == 1:
        odd_list.append(i)
        # print(i)

print(odd_list)