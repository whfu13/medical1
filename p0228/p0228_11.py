num = [100,200,300,400]
# for문을 사용해서 하나씩 출력해보세요 2가지 방법 다 쓰기
for n in num:
    print(n,end='\t')
print()

for i in range(len(num)):
    print(num[i],end='\t')
    
f = [['딸기', 100, 1000],['수박', 100, 500],
     ['사과',100,1200],['귤',100,300]]

# 요소 한개한개를 출력해보세요
print(f[0][0]), (f[1][0]), (f[2][0]), (f[3][0])
for i in range(len(f)):
    print(f[i][0])

for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j],end=' ')

print()

score = [90,80,70,100,95,85,100]
# 점수의 총합을 구하세요

t = 0
for n in score:
    t += n
    
print(t)
    
total = []

for i in range(7):
    print(score[i])
    
# 토탈 점수 계산
total.append(t)
    
print(total)