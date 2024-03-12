from random import *
# 1. 변수선언 1 - 10
lotto = []
# 2. 입력받은 숫자 6개
mynum = [2,5,1,9,3,7]
l = []
# 3. 로또 번호 생성하기
for i in range(6):
    n = randint(1,10)
    lotto.append(n)
print(lotto)

num = [1,2,3,4,5,6,7,8,9,10] # 특징 : 중복이 없다, 1-10까지다
for i in range(100):
    tmp = randint(0,9)
    # print(tmp)
    num[0],num[tmp] = num[tmp], num[0]
    # print(num)

print(num)

for i in range(6):
    lotto.append(l[i])
    
print(lotto) 
ok = []
if i in range(len(mynum)):
    # print(mynum[i])
    if mynum[i] in lotto:
        ok.append(mynum[i])
        
print(ok)