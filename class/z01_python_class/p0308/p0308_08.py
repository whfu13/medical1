import random

a = "1조123456"
b = "9조777776"

cnt = 0
for i in range(len(a),0,-1):
    if i==2: continue # 조는 건너뛰기
    if a[i-1] != b[i-1]:
        break
    else:
        cnt += 1 # 맞는 횟수 1증가
if cnt == 0:
    print("완전 꽝입니다.")
elif cnt == 1:
    print("6번째 자리가 맞았습니다. 당첨금액 : 1만원")
elif cnt == 2:
    print("5,6번째 자리가 맞았습니다. 당첨금액 : 10만원")
elif cnt == 3:
    print("4,5,6번째 자리가 맞았습니다. 당첨금액 : 100만원")
elif cnt == 4:
    print("3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 1000만원")
elif cnt == 5:
    print("2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 1억")
elif cnt == 6:
    print("1,2,3,4,5,6번째 자리가 맞았습니다. 당첨 금액: 10억원")
# for i in a:
#     print(a[0])
# first_num = random.randint(1,9)
# last_num = random.randint(0,999999)
# # lotto = "1조740042"
# lotto = str(first_num)+"조"+"{:6d}".format((last_num))
# print(lotto)
# l_input = input("복권을 입력하세요.(예:1조111)")
# # 비교하는 프로그램을 구현하시오.
# # 자리수를 활용하세요.
# cnt = 0
#     # if lotto(a[-1]) == l_input[i]:
#     #     cnt += 1
        
# print("맞는개수 : ",cnt-1)