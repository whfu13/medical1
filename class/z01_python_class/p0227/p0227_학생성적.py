student = []
# for를 사용해서 5번 반복
for i in range(5):
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력')  # if 문을 사용해서 1 누르면 [학생성적입력]
    print('4.학생성적전체출력') # 4를 누르면 [학생성적전체출력
    print('0.프로그램 종료') # 0을 누르면 [프로그램종료]
    print('-'*35)
    ch = input('원하는 번호를 입력하세요 >> ')
    print(ch)
    if ch == '1':
        print('학생성적입력')
        # 이름, 국, 영,수 점수를 입력받아
        stu_name = input("이름을 입력하세요 >> ")
        kor = int(input("국어점수를 입력하세요 >> "))
        eng = int(input("영어점수를 입력하세요 >> "))
        math = int(input("수학점수를 입력하세요 >> "))
        total = kor+eng+math
        avg = (kor+eng+math)/3
        stu1 = [3,stu_name,kor,eng,math,kor+eng+math,(kor+eng+math)/3, 0]
        
        student.append(stu1)
        print(student)
       
    elif ch == '4':
        print('학생성적전체출력')
        # 출력 for를 사용해서 학생 수 만큼 출력
        for i in range(len(student)):
             print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                 student[i][0],student[i][1],student[i][2],
                 student[i][3],student[i][4],student[i][5],
                 student[i][6],student[i][7]))
    elif ch == '0':
        print('프로그램종료')
    else:
        print('잘못입력하셨습니다')            
    
    print('*'*35)

print('프로그램이 종료되었습니다')

    