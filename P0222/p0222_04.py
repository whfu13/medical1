# 두수를 입력받아서 사칙연산을 출력해보세요
# 변수 n1, n2
# 출력
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.333

# 1. 문자열로 4줄 출력
print('{}+{}={}'.format(10,3,10+3))
print('{}-{}={}'.format(10,3,10-3))
print('{}*{}={}'.format(10,3,10*3))
print('{}/{}={}'.format(10,3,10/3))
# 2. n1 = 10, n2 = 3 변수를 선언해서 4줄 출력
n1 = 10
n2 = 3

print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={}'.format(n1,n2,n1/n2))
# 3. n1, n2 입력 받아서 4줄 출력
n1 = input("첫번쨰 숫자를 입력하세요 >> ")
n2 = input("두번쨰 숫자를 입력하세요 >> ")

n1 = int(n1)
n2 = int(n2)
print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={}'.format(n1,n2,n1/n2))