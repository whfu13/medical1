# 리스트
# 1-10까지 입력
# 1. list 기본문접
list= []
for i in range(1,11):
    list.append(i)
    
list = [0]*10 # 2. 공간을 먼저 만들고
for i in range(10):
    list[i] = i+1

# 3. 컴프리헨션
# list = [i for i in range(1,11)]   
print(list)

    