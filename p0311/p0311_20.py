students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]

cnt = len(students)+1
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print("숫자만 입력 가능합니다.")
        continue
    choice = int(choice)
    
    # 1. 학생성적입력
    if choice == 1:
        while True:
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
            if(name=="0"):
                print("학생 입력을 취소합니다.")
                break
            student = {}
            student["stuNo"] = "S"+"{:03d}".format(cnt)
            student["name"] = name
            kor = int(input("국어점수를 입력하세요."))
            student["kor"] = kor
            eng = int(input("영어점수를 입력하세요."))
            student["eng"] = eng
            math = int(input("수학점수를 입력하세요."))
            student["math"] = math
            total = kor+eng+math
            student["total"] = total
            avg = total/3
            student["avg"] = float("{:.2f}".float(avg))
            students.append(student)
            cnt += 1
            print("입력 데이터 :",student)
            print(students)
            
    # 2. 학생성적출력
    elif choice == 2:
        count = input("학생성적 전체 출력을 하시겠습니까? (1.확인, 0.취소)")
        if count == "0":
            break
        print("\t[학생성적전체출력]")
        print("-"*65)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        print("-"*65)
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()
        print('-'*65)
        print()
        
    # 3. 학생검색
    elif choice == 3:
        pass
    
    # 4. 학생수정
    elif choice == 4:
        s_title = ['','국어','영어','수학']
        while True:
            search = (input("검색하고 싶은 학생의 이름을 입력하세요."))