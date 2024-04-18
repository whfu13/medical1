# 돈을 입력받아
# 5만원권
# 만원권
# 오천원권
# 천원권으로 교환해서 출력

money = input("교환할 돈을 입력하세요")
money = int(money)
money = 245678000

c50000 = money//50000
c10000 = (money%50000)//10000
c5000 = (money%50000)%10000//5000
c1000 = (((money%50000)%10000)%5000)//1000

print('입력한 금액 : {}'.format(money))
print('50000원 : {}'.format(c50000))
print('10000원 : {}'.format(c10000))
print('5000원 : {}'.format(c5000))
print('1000원 : {}'.format(c1000))