from random import *
# 랜덤한 숫자를 만들어 (1-100 사이)
# 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨(프로그램 종료)
# 아니면 다시 입력
# 를 출력하는 무한
print(randint(1,100))
print(randint(1,100))
print(randint(1,100))
print(randint(1,100))

randnum = randint(1,100)
# 입력한 숫자가 랜덤숫자보다 작으면 더 큰수를 입력
# 입력한 숫자가 랜덤숫자보다 크면 더 작은수를 입력
# 1. 현재 입력한 숫자 모두를 inputList에 넣으세요
inputList = []
# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요   
cnt = 0     
while cnt < 10 :
    cnt += 1
    n = int(input('{}번째 도전! 숫자를 입력하세요 >>'.format(cnt)))
    inputList.append(n)
    if randnum == n:
        print('당첨')
        break
    elif n > randnum:
        print('입력하신 숫자가 랜덤숫자보다 큽니다.')
        print('더 큰수를 입력해주세요 >> ')
    else:
        print('입력하신 숫자가 랜덤숫자보다 작습니다.')
        print('더 작은수를 입력해주세요 >> ')
        
# 3. 10회 도전이 실패한 사람에게 랜덤숫자 알려주기
if cnt == 10:
    print('10회 입력을 초과하셨습니다. 정답은',randnum)
        
print('사용자가 입력한 숫자들은 :',inputList)