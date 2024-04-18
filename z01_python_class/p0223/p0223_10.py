# 해보세요
# 성별, 키를 입력받아서
# 남자일 경우(m) 172.5 이상이면 [평균이상] 이하면 [평균이하]
# 여자일 경우(f) 159.6 이상이면 [평균이상] 이하면 [평균이하]
# 그 외는 [잘못입력하셨습니다] 라고 출력해보세요
gender = input('성별을 입력하세요 >> ')
height = float(input('키를 입력하세요 >> '))


if gender == "남자" :
    print("m")
    if height >= 172.5 :
        print("평균이상")
    else:
        print("평균이하")    
elif gender == "여자" :
    print("f")    
    if height >= 159.6 :
        print('평균이상')
    else:
        print('평균이하')    
else:
    print('잘못입력하셨습니다')      