num = []
# for문을 사용해서 1-10 까지 숫자를 num에 채우세요
for i in range(1,11):
    num.append(i)
    print(num)
    
# 한줄로 표현 할 수 도있다.

num2 = []
# 1-10까지의 짝수를 num2리스트에 넣으세요
for i in range(1,11):
    if i % 2 == 0:
        num2.append(i)
        # print(i)
        
print(num2)

# 1 ~ 10까지의 합 for문을 사용해서 구할 수 있음.
num = [1,2,3,4,5,6,7,8,9,10]
    #  0 1 2 3 4 5 6 7 8 9
# num 리스트를 사용해서 1-10까지의 합을 구해보세요
s1 = 0 # 최종 더하기에 사용될 변수
for i in range(1,11):
    s1 += i
print(' 1-10까지의 합은: {}입니다'.format(num))
s2 = 0
for i in range(len(num)):
    s2 = s2 + num[i]
# num 리스트 내의 숫자들의 합을 구하세요
s3 = 0
for i in num2:
    s3 = s3

# num2 리스트 내의 숫자들의 합을 구하세요
s4 = 0
for i in range(len(num2)):
    s4 = s4+num2[i]
print(s3,s4)