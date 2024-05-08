# 학생 이름, 국어, 영어, 수학 점수를 입력받아서
# 아래와 같이 출력을 하고

# 만약에 평균이 80점이상이면 합격입니다를 출력하세요

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}t{}\t{}\t{}\t{}\t{}\t{}'.format(
    1, '홍길동', 100,100,100,300,100.0,1))

stu_name = input("이름을 입력하세요")

kor = 100
eng = 100
math = 100
total = kor+eng+math
avg = (total)/3

kor = int(input("국어점수를 입력하세요"))
eng = int(input("영어점수를 입력하세요"))
math = int(input("수학점수를 입력하세요"))
total = kor+eng+math
avg = (total)/3

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}t{}\t{}\t{}\t{}\t{}\t{}'.format(
    1, stu_name, kor,eng,math,total,avg,1))

if avg >= 80 :
    print("홍길동님 합격입니다")
else:
    print("홍길동님 불합격입니다")   