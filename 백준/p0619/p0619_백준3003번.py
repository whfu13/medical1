# 백준 3003번
a_list = [1,1,2,2,2,8]

b_list = list(map(int,input().split(" ")))

for i in range(6):
    print(a_list[i]-b_list[i], end = ' ')
