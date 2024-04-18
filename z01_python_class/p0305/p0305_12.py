import operator

# 딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

print(sorted(t_dic.items(),key=operator.itemgetter(0)))
# (peach,복숭아),(orange,오렌지)...

# print(t_dic.keys()) # 키값
# print(t_dic.values()) # value값
# print(t_dic.items()) # 튜플

# 3개의 숫자를 입력받아 순서대로 출력하세요.
# 17,50,12
# num = [0,0,0]
# for i in range(3):
#     num[i] = int(input(f"{i+1}번째 숫자를 입력하세요 >> "))
#                   input("{}번째 숫자를 입력하세요.".format(i+1))

# print("최대값 : ",max(num[0],num[1],num[2])) # *num
# print("최소값 : ",min(num[0],num[1],num[2]))
# print(num)

# # a = [5,7,4,8,1,9,3,2]
# a.sort() # 순차정렬
# print(a)
# print("-"*50)
# b= [5,7,4,8,1,9,3,2]
# b.sort(reverse=True)# 역순정렬
# print(b)