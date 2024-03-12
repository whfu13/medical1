# 구구단 - 이중 for문을 사용
temp = 0
# 변수를 1개 사용
for i in range(1,10):
    for j in range(1,10):
        if j == 5:
            temp = 1
            break
        print(f"{i} * {j} = {i*j}")
    if temp == 1: break