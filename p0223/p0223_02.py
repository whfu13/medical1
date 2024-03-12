# 1. 숫자 두개를 입력받아서 나누기값 몫값 나머지값을 출력

n1 = int(input("첫번째 숫자를 입력하세요 >> "))
n2 = int(input("두번째 숫자를 입력하세요 >> "))

print("나누기값은 {}입니다".format(n1/n2))
print("몫값은 {}입니다".format(n1//n2))
print("나머지값은 {}입니다".format(n1%n2))

# 2. 3개의 수의 합을 구하세요
s1, s2, s3 = '100', '100.123', '99.9'

s1 ='100'
s2 ='100.123'
s3 = '99.9'

a1 = int(s1)
a2 = float(s1)

result = (int(s1)+float(s2)+float(s3))
print('합은 {}입니다'.format(result))
