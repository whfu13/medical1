# 리스트에 1,25까지 숫자를 리스트에 입력하시오
num = []
for i in range(0,25):
    num.append(i+1)
    
print(num)
print("-"*40)

# 1부터 25까지 2차원 리스트 생성
# [[1,2,3,4,5],[6,7,8,9,10],....,[21,22,23,24,25]]
list = []
l = []

for i in range(0,25):
    if(i+1)%5 == 0:
        l.append(i+1)
        list.append(l)
        l=[] 
    else:
       l.append(i+1) # [1,2,3,4]
    l.append(list)
    
print(list)



        