# 조건문
# 1. 키가 130cm 이상만 놀이기구를 탑승할 수 있다.
height = 120
if height >= 130 :
    print("놀이기구 탑승 가능")
else:
    print('놀이기구 탑승 불가능')    
# 조건문

# 2. 나이가 10살 이상이고 키가 130 이상만 놀이기구 탑승가능
age = 11
if age >= 10 and height >= 130 :
    print("나이가 {}살 이여서 탑승이 가능합니다.".format(age,height))

#3. 비 면 [우산을 챙겨주세요]
# 아니면 [선크림발라주세요] 출력
weather ='비'
if weather == '비':
    print('우산을 챙겨주세요')
else:
    print('선크림을 발라주세요')    

# 4. 비 나 눈이면 [우산을 챙겨주세요]
# 아니면 [선크림발라주세요] 출력
weather = '맑음'
if weather == '비' or weather == '눈':
    print('우산을 챙겨주세요')
else:
    print('선크림을 발라주세요')    
