# str1 = '10'
# print(str1.isdigit()) # True

# str2 = 'a'
# # n은 문자열
# while True:
#     n = input('원하는 번호를 입력해주세요')
#     if n.isdigit(): # 숫자지만 문자열 ex) "o" '1'
#         n = int(n)
#     else:
#         print('문자가 입력되었습니다. 다시 입력해주세요')

#     n = int(input('원하는 번호를 입력해주세요'))
#     if n == 0:
#         print('숫자0이 입력되었습니다')

# 이름을 검색해보고, 이름을 검색해서 삭제
students = [[1, '홍길동',100],[2, '이순신',90], [3, '유관순',85],
            [4, '김유신',70], [5, '김구', 95]]
while True:
    print('1.학생 검색')
    print('2.학생 삭제')
    print('3.프로그램 종료')
    ch = input('원하는 번호를 입력해주세요 >> ')
    if ch.isdigit(): # 입력한게 숫자면 True
        ch = int(ch)
    if ch == 1: # 1. 학생 검색
        searchName = input('검색할 학생의 이름을 입력하세요 >> ')
        chk = 0 # chk = 0일때는 학생이 존재하지 않음. chk=1일때는 학생이 존재
        for stu in students:
            # print(stu)
            if searchName in stu:
                print('{} 학생이 존재합니다.'.format(searchName))
            print(stu)
            chk = 1
    elif ch == 2: # 2.학생 삭제
        delName = (input('삭제하고 싶은 학생의 이름을 입력하세요 >> '))
        for i, stu in enumerate(students):
            if delName in stu :
                del(students[i])
        print(students)
                
    elif ch ==  3:
        print('프로그램이 종료되었습니다.')
        break # 반복문 종료
    else:
        print('잘못입력하셨습니다. 다시 입력해주세요')