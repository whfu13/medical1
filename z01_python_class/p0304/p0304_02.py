# 숫자 1개를 입력받아 1개 출력하세요
# 1. 숫자 1개 입력
# 2. 숫자 1개 출력
num = int(input('숫자를 입력하세요'))
num2 = int(input('숫자를 입력하세요'))
print(num)
print(num2)
print(num+num2)

nums = []
for i in range(0,5):
    nums.append(int(input('숫자를 입력하세요')))
    
print(nums)

# 5개의 합을 구하세요
sum = 0

for num in nums:
    sum += num
print('합계 : ', sum)    