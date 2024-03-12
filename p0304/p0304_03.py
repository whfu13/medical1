# 2명의 학생의 국어, 영어, 수학을 입력받아
# 합계를 출력하세요
students = []
for i in range(0,2):
    student = [] # 초기화
    
student.append(input('이름을 입력하세요.'))
student.append(int(input("국어점수를 입력하세요 >> ")))
student.append(int(input("영어점수를 입력하세요 >> ")))
student.append(int(input("수학점수를 입력하세요 >> ")))
sum = student[1]+student[2]+student[3]
student.append(sum)
student.append('{:.2f}'.format(sum/3))
students.append(student)
# 합계
print(student)
# 전체학생출력
print("[학생성적 출력]")
print('-'*50)
print("이름\t국어\t영어\t수학\t합계\t평균\n")
print("-"*50)
# 전체 출력
for stu in students:
    for s in stu:
        print(s,end="\t")
    print()
print('-'*50)
# 총학생의 총국어점수, 총영어점수, 총수학점수, 총합계, 총평균
# 2차원 리스트는 for문을 2번 사용함.
# 3명의 국어점수 합계,평균을 출력
kors = 0
engs = 0
maths = 0
totals = 0
avgs = 0
for i,stu in enumerate(students):
    kors = kors + stu[1]
    engs = engs + stu[2]
    maths = stu[3]
    totals = stu[4]
    
avgs = totals/len(students)    
print('\t')
print(kors,engs,maths,totals,avgs,sep='\t')    