# 국어, 영어, 수학 점수를 입력받아서 평균을 출력하세요
# 출력 : 평균은 : 95점입니다.
# 변수 : kor, eng, math

# 변수 선언해서 출력
# kor = 100, eng = 90, math= 80

# 3가지 점수를 입력받아서 출력

kor = 100
eng = 90
math = 80
avg = (kor+eng+math)/3

print('평균은 : {}점 입니다'.format(avg))

kor = 100
eng = 90
math = 80

print('평균은 : {}점 입니다'.format(kor+eng+math/3))

kor = input("국어점수 :")
eng = input("영어점수 :")
math = input("수학점수 :")

kor = int(kor)
eng = int(eng)
math = int(math)
avg = (kor+eng+math)/3
print('평균은 : {}점 입니다'.format(avg))