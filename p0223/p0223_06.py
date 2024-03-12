# if - else
# if - elif - else
'''
if 조건문1 :
   실행문1
elif 조건문2 :   
     실행문2
else:
    실행문3

조건문1이 참이면 실행문1 실행 후 종료
조건문1이 거짓이고 조건문2가 참이면 실행문2 실행후 종료
조건문1, 조건문2가 거짓이면 실행문3 실행 후 종료
'''
weather = '비'
if weather == '비' :
    print('비가 오네요 우산을 챙겨주세요')
elif weather == '눈':
    print('눈이 옵니다 조심하세요')
else:
    print('선크림을 발라주세요')        