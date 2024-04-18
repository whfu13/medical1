list = []

# 1-9까지의 숫자를 1차원 리스트에 입력
for i in range(9):
    list.append(i+1)
print(list)

list2 = [n+1 for n in range(9)]
print(list2)

list3 = [[n]*3 for n in range(3)]

numList = [num*num for num in range(1,6)]
print(numList)

# 1-9까지의 숫자를 2차원 리스트에 입력
# a_lists = []
# for i in range(3):
#     a_list = []
#     for j in range(3):
#         a_list.append(3*i)+(j+1) # [0,1,2]
#     a_lists.append(a_list) # [0,1,2],[0,1,2],[0,1,2]
        
# print(a_lists)
    
# for i in list:
#     for f in i:
#         print(f,end="\t")
#     print()
    
    