import random
# 크기가 10인 리스트 생성하는데, 7개는 0으로 3개는 1로 채우시오.
# [1,1,1,0,0,0,0,0,0]

# list = [0]*10
# for i in range(3):
#     list[i] = 1
# print(list)

# 크기가 100인 리스트 생성, 10개는 1로 채우시오.
# 랜덤으로 섞어서 출력

# list = [0]*100
# for i in range(1):
#     list[i] = i+1
#     random.shuffle[list]
# print(list)

aList = [0 for i in range(100)]
print(aList)
for i in range(10):
    aList[i] = 1
    
print(aList)
random.shuffle(aList)
print(aList)

# [ 10*10 ] 2차원 배열을 생성하시오.
bLists = []
bList = []
for i,j in enumerate(aList):
    if (i+1)%10 == 0:
        print(i)
        bList.append(j)
        bLists.append(bList)
        bList = [] # 100번 계속 처음으로 초기화
    else:
        bList.append(j)
        
newLists = [["추첨"]*10 for _ in range(10)]

cnt = 0 # 당첨횟수
while True:
    print(bLists)
    print("[ 10*10 좌표 ]")
    print("-"*60)
    # print(bList)
    print("",0,1,2,3,4,5,6,7,8,9,sep="   ")
    print("-"*60)
    for i,b in enumerate(newLists):
        print(i,end=" ")
        for bb in b:
            print(bb,end=" ")
        print()
    print("-"*60)
    x = int(input("가로 좌표를 입력하세요."))
    y = int(input("세로 좌표를 입력하세요."))
    # bLists - 값을 비교, newLists - 표시
    if bLists[x][y] == 1: #당첨
        newLists[x][y] = "당첨"
        cnt += 1
        if cnt == 2:
            print("모두 당첨되었습니다.")
            break
    else: # 꽝
        newLists[x][y] = "[꽝]"