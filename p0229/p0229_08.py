# 1-100까지 더하는데,
# 총 합이 100이 넘었을때 총합과 그 수를 출력하세요

# ex) 1-10까지 더하는데 총합이 4가 넘는 수를 출력
# 1+2+3 총합 : 6 수: 3
sum = 0
for i in range(1,11):
    sum += i
    if sum > 4 :
        break
    
print('수: ', i)
print('총합 :',sum)

for i in range(1,101):
    sum += i
# print(sum)
    if sum > 100:
        break 
    
print('수: ', i)
print('총합 :',sum)