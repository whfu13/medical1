fruits = ['딸기','사과','자몽','포도','수박','자몽']

# 만약에 자몽을 삭제
# 리스트명.remove('요소명')
# print(fruits)
# fruits.remove('자몽')
# print(fruits)
# del(리스트명[번호])
del(fruits[5])
print(fruits)

for index, elem in enumerate(fruits):
    print('{}는 {}번째에 있습니다.'.format(elem,index))