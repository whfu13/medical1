from random import *
# 1 - 45까지의 숫자를 넣어서

mynum = [] # 입력을 1 - 45 사이의 숫자를 입력을 받음
lotto = [] # 1 - 45 사이의 랜덤한 숫자 6자리 저장
l = []
ok = []

for i in range(6):
    a = int(input("입력하신 숫자를 넣어주세요 >> "))
    mynum.append(a)
    

print(mynum)
print(lotto)

for i in range(1,46):
    l.append(i)
# l 리스트에 1-45 중복이 없는 1-45까지의 숫자가 들어있음
print('로또 숫자 : {}'.format(l))

for i in range(100):
    tmp = randint(0,44)
    l[0],l[tmp] = l[tmp],l[0]
    
print('로또 숫자 : {}'.format(l))

# 1 잘섞여있고, 중복없음
    
for i in range(6):
    lotto.append(l[i]) 

# 랜덤하고 중복이 없는 숫자 6개 생성
print('로또 숫자 : {}'.format(lotto))    
    
# m = [1,2,3] l = [3,6,7] 3, 1개 [3]
# lotto = [1,2,3,4,5,6,]
# mynum = [7,8,9,10,5,7]
if i in range(6): # i = 0,1,2,3,4,5
    if mynum[i] in lotto:
        ok.append(mynum[1])
print('입력한 숫자 : {}'.format(mynum))   
print('로또 숫자 : {}'.format(lotto))   
print('당첨된 숫자 : {}'.format(ok))   