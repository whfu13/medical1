# a =[[],[],[],[],[]]
# 리스트 공간초기화를 먼저 해줘야함.
a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# a = [[0]*5] *5
# value = 1
for i in range(0,5): # 0,1,2,3,4
    for j in range(0,5): # 0,1,2,3,4
       a[i][j] = (5*i)+j+1 # value
       # value += 1
         
print(a)