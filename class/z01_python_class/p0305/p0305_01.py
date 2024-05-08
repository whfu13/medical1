# 리스트에 1,25까지 숫자를 리스트에 입력하시오
num = []
for i in range(0,25):
    num.append(i+1)
    
print(num)

# 1부터 25까지 2차원 리스트 생성
# [[1,2,3,4,5],[6,7,8,9,10],....,[21,22,23,24,25]]
l = []
list = []

for i in range(0,25):
    if(i+1)%5 == 0:
        for j in range(25):
            list.append(i)
    l.append(list)
    
print(l)