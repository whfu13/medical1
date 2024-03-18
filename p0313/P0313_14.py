import random

c_number = [0]*13
for i in range(13):
    c_number[i] = i+1

c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# 랜덤으로 숫자 2개를 뽑아서 출력하시오.
choice = random.sample(c_number,k=2)
print(choice)

# 랜덤숫자 : ? => ?번방에 있습니다.
# 랜덤숫자 : ? => ?번방에 있습니다.
# 큰수 : ?, 작은수 : ?
print(f"랜덤숫자: {choice[0]} => {choice[0]-1}번 방에 있습니다.")
print(f"랜덤숫자: {choice[1]} => {choice[1]-1}번 방에 있습니다.")

if choice[0] > choice[1]:
    print(f"큰 수 :{choice[0]}, 작은 수 :{choice[1]}")
else:
    print(f"큰 수 :{choice[1]}, 작은 수 :{choice[0]}")
    