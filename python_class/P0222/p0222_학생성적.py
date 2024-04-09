print('-'*35)
print('\t[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    1, '홍길동', 100,100,100,300,100.0,1))
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    2, '유관순', 90,100,90,300,93.3,1))

# 홍길동 100 100 100
# 유관순 90  100 90

stu_name1 = input('첫번쨰 학생이름을 입력하세요  >>')
# kor1 = 100
# eng1 = 90
# math1 = 80

kor1 = int(input("첫번쨰 학생의 국어점수를 입력하세요 >> :"))
eng1 = int(input("첫번째 학생의 영어점수를 입력하세요 >> :"))
math1 = int(input("첫번째 학생의 수학점수를 입력하세요 >> :"))
total1 = kor1+eng1+math1
avg1 = (total1)/3


stu_name2 = input('두번쨰 학생이름을 입력하세요  >>')
kor2 = int(input("두번쨰 학생의 국어점수를 입력하세요 >> :"))
eng2 = int(input("두번째 학생의 영어점수를 입력하세요 >> :"))
math2 = int(input("두번째 학생의 수학점수를 입력하세요 >> :"))
total2 = kor2+eng2+math2
avg2 = (total2)/3


print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    1, stu_name1, kor1, eng1, math1, total1, avg1, 1))
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    2, stu_name2, kor2, eng2, math2, total2, avg2, 1))


