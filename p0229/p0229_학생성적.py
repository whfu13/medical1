student = []
cnt = 0
while True:
    print('-'*35)
    print('\t+[학생성적프로그램]')
    print('-'*35)
    print('1.학생성적입력')
    print('2.학생성적수정')
    print('3.학생성적삭제')
    print('4.학생성적전체출력')
    print('5.학생검색출력')
    print('6.등수처리')
    print('0.프로그램종료')
    print('-'*35)
    choice = input('원하는 번호를 입력하세요 >> ')
    print('입력하신 번호는 {}입니다'.format(choice))
    if choice == '1':
        print('학생성적입력')
        stu_name = input('학생의 이름을 입력하세요 >> ')
        kor = int(input('국어점수를 입력하세요 >> '))
        eng = int(input('영어점수를 입력하세요 >> '))
        math = int(input('수학점수를 입력하세요 >> '))
        total = kor+eng+math
        avg = (total)/3
        stu1 = [3,stu_name,kor,eng,math,total,(kor+eng+math)/3, 0]
        
        student.append(stu1)
        print(student)
    elif choice == '2':
        reName = input('수정하고싶은 학생의 이름을 입력하세요 >> ')
        for i,m in enumerate(student):
            if reName in m:
                print(reName,'님을 선택하셨습니다.')
                choice_num = input('수정하고 싶은 항목을 선택해주세요 >>')
                if choice_num == '1':
                    print(reName,'님의 번호 수정을 선택하셨습니다.')
                    print(reName,'님의 번호는',student[i][0],'입니다.')
                    stu_num = input('새로운 번호를 입력하세요 >>')
                    stu_num = int(stu_num)
                    student[i][0] = stu_num
                elif choice == '2':
                    print(reName,'님의 이름 수정을 선택하셨습니다.')
                    print(reName,'님의 이름은',student[i][0],'입니다.')
                    stu_name = input('새로운 이름을 입력하세요 >> ')
                    student[i][1] = stu_name
                    
    elif choice == '3':
        delName = input('삭제하고 싶은 학생의 이름을 입력하세요 >> ')
        for i,m in enumerate(student):
            if delName in m:
                del(student[i])
                print('삭제되었습니다'.format(delName))
    elif choice == '4':
        for i in range(len(student)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format
                (student[i][0],student[i][1],student[i][2],
                 student[i][3],student[i][4],student[i][5],
                 student[i][6],student[i][7]))
    elif choice == '5':
        searName = input('검색하고싶은 학생의 이름을 입력하세요 >> ')
        for i,m in enumerate(student):
            if searName in m:
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format
                (student[i][0],student[i][1],student[i][2],
                 student[i][3],student[i][4],student[i][5],
                 student[i][6],student[i][7]))

    elif choice == '0':
        print('프로그램종료')
        break
    else:
        print('잘못입력하셨습니다')            
    
    print('*'*35)

print('프로그램이 종료되었습니다')

    