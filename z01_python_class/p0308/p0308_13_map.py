# map => 문자열을 정수형으로 모두 변환해서 리스트 저장
today_list = ['2024','03','08']
# today_list[0] = int(today_list[0])+10
# print(today_list[0])
t_list = list(map(int,today_list))
print(t_list)

# map => 정수형을 문자열로 모두 변환해서 리스트 저장
int_list = [10,20,30,40,50]
str_list = list(map(str,int_list)) # int => str
print(str_list)
# 5개의 숫자를 입력하시오.


# 함수를 사용하여 리스트의 값을 *10 변경 map
# 리스트의 데이터 타입: int
# list = []
# for i in range(5):
#     list.append(i) # 데이터타입 : int
    
# print(list)

# 리스트의 데이터 타입: str
# a_list = list(map(str,range(10)))
# print(a_list)

a_list = list(map(int,input("숫자입력:")))
print(a_list)