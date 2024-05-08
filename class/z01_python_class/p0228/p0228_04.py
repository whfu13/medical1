# 1-100까지의 합
# 1- 100까지 짝수의 합, 홀수의 합 if절을 사용
s1,s2,s3 = 0,0,0

for i in range(1,101):
    s1 += i
    if i % 2 == 0:
        s2 += i
    else: # 홀수
        s3 += 1
    print('1부터 100까지 합은 {}입니다'.format(s1))
    print('1부터 100까지 짝수의 합은 {}입니다'.format(s2))
    print('1부터 100까지 홀수의 합은 {}입니다'.format(s3))

# 1- 10까지의 합
s10 = 0
for i in range(1,11):
    s10 += i
    print('1부터 10까지의 합은: {}입니다'.format(s10))
#
# num 리스트 안에 있는 값들의 합
num = [1,2,3,4,5,6,7,8,9,10]

t = 0
for n in num:
    t += n
    # print(n)
print('num리스트의 합 : {}'.format(t))

t1 = 0
for i in range(len(num)):
    t1 += num[i]
    
print('num리스트의 합 : {}'.format(t1))
    