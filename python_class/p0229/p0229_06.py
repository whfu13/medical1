# continue 예제
# 1 - 100 합계를 구하는데 3의 배수는 제외하고 더하기
# while or for 사용
for i in range(1,101):
    print(i,end=' ')
    
for i in range(1,101):
    if i % 3 == 0:
        continue
    print(i,end=' ')
print()

for i in range(1,101):
    if i % 3 == 0:
        continue
    print('1-100 3의 배수 제외한 합()')