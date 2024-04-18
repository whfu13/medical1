print('2단 출력')
for i in range(1,10): # i = 1,2,3,4,5,..9
    print('2 * {} = {}'.format(i, 2*i))
    
# 원하는 단을 입력받아서 구구단을 입력하세요
# 3을 입력받으면 3단 출력.

n = int(input("원하는 단을 입력하세요 >> "))
print('3단 출력')
for i in range(1,10):
    print('{} * {} = {}'.format(n, i, n*i))
    
# 5번 반복

for i in range(5):
   n = int(input("원하는 단을 입력하세요 >> "))
   for i in range(1,10):
       print('{} * {} = {}'.format(n, i, n*i))

