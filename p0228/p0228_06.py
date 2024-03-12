from random import *

n1 = randrange(1,11) # 1 - 10까지의 정수
n2 = randint(1,10) # 1 - 10까지의 정수

# 랜덤한 숫자 6개 lotto리스트에 넣고
# 내가 입력한 숫자 6개는 mynum리스트에 넣어주세요
lotto = []
mynum = []

for i in range(6):
    a = randint(1,10)
    lotto.append(a)
    
print(lotto)

for i in range(6):
    b = int(input("숫자를 입력하세요 >> "))
    mynum.append(b)
    
print(mynum)

# 중복없이 숫자를 입력받고싶다.
for i in range(6):
    a = randint(1,10)
    # 만약에 랜덤숫자(a)가 lotto리스트에 없다면
    if a not in lotto:
        lotto.append(a) # 추가해라