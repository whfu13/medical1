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
        print("숫자만 입력이 가능합니다.")
        continue
    choice = int(choice)
    
    # 1. 학생성적입력
    if choice == 1:
        while True:
            name = input(f"{len(students)}번째 학생이름을 입력하세요(0.취소)")
            if(name =="0"):
                print("학생 입력을 취소합니다")
                break
            student = {}
            student["stuNo"] = "S"+"{:03d}".format(cnt)
            student["name"] = name
            kor = int(input("국어점수를 입력하세요 >>"))
            student["kor"] = kor
            eng = int(input("영어점수를 입력하세요 >>"))
            student["eng"] = eng
            math = int(input("수학점수를 입력하세요 >>"))
            student["math"] = math
            total = kor+eng+math
            student["total"] = total
            avg = total/3
            student["avg"] = float("{:.2f}".format(avg))
            students.append(student)
            cnt += 1
            print("입력 데이터:",student)
            print(students)
            
    # 2. 학생성적전체출력        
    elif choice == 2:
        count = input("학생성적을 전체출력하시겠습니까? (1. 확인, 0.취소) ")
        if count == "0":
            break
        print("[ 학생성적전체출력 ]")
        print('-'*65)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print('-'*65)
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()
        print('-'*65)
        print()
        
    # 3. 학생검색
    elif choice == 3:
        while True:
            search = input("검색하고싶은 학생의 이름을 입력하세요 >> ")
            chk = 0
            count = 0
            if search == "0":
                break
            for stu in students:
                if search in stu:
                    chk = 1
                    break
                count += 1
            if(chk == 1):
                print("{} 학생성적출력 ".format(search))
                print('-'*50)
                print("")
                print('-'*50)
                print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
                for i in students[count]:
                    print(i,end='\t')
                print()
            else:
                print("찾는 학생의 정보가 없습니다.")
                
    # 4. 학생수정
    elif choice == 4:
        s_title = ['','국어','영어','수학']
        while True:
            search = input("찾는 학생의 이름을 입력하세요.(0.취소)")
            chk = 0
            if search == "0":
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk +=1
                
            print("찾고자 하는 학생의 위치",chk)
                         
            if chk == len(students):
                print(f"{search} 학생은 없습니다. 다시 입력하세요 ")
            else:
                print(f"{search} 학생을 찾았습니다. ")
                while True:
                    print("[ 수정할 과목 선택 ]")
                    print('-'*30)
                    print('1.국어\t2.영어\t3.수학')
                    s_input = int(input("수정할려는 과목을 선택하세요 (0.취소) >> "))
                    if s_input == 1:
                        s_1 = "kor"
                        print("[{} 수정]".format(s_title[s_input]))
                        print("현재 {} 점수: {}".format(s_title[s_input],students[chk][s_1]))
                        print('-'*20)
                        score = int(input("수정할 {}점수를 입력하세요".format(s_title[s_input])))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                        
                        print("{}점수: {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                        print(students[chk])  
                           
                    elif s_input == 2:
                        s_1 = "eng"
                        print("[{} 수정]".format(s_title[s_input]))
                        print("현재 {} 점수: {}".format(s_title[s_input],students[chk][s_1]))
                        print('-'*20)
                        score = int(input("수정할 {}점수를 입력하세요".format(s_title[s_input])))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                        
                        print("{}점수: {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                        print(students[chk])     
                    
                    elif s_input == 3:
                        s_1 = "math"
                        print("[{} 수정]".format(s_title[s_input]))
                        print("현재 {} 점수: {}".format(s_title[s_input],students[chk][s_1]))
                        print('-'*20)
                        score = int(input("수정할 {}점수를 입력하세요".format(s_title[s_input])))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                        
                        print("{}점수: {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                        print(students[chk])     
                    
                    else:
                        print("과목 수정을 취소합니다. ")
                        break
    
    # 5. 학생 등수처리
    elif choice == 5:
        for i,s_dic in enumerate(students):
            rank_cnt = 1
            for i_dic in students:
                if s_dic["total"] < i_dic["total"]:
                    rank_cnt += 1
                s_dic["rank"] = rank_cnt
                
            print("등수처리가 완료되었습니다.")
            print()
                
    # 6. 학생 삭제      
    elif choice == 6:
        while True:
            search = input("찾는 학생의 이름을 입력하세요. (0.취소 )")
            chk = 0
            if search == "0":
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk += 1
                
            print("찾고자 하는 학생의 위치: ",chk)
            
            if chk >= len(students):
                print("찾고자 하는 학생이 없습니다.")
            else:
                print("{} 학생을 찾았습니다.".format(search))
                s_input = input("{} 학생 성적을 삭제하시겠습니까?(1.실행 0.취소)".format(search))
                if s_input != "1":
                    print("삭제를 취소합니다.")
                    break
                else:
                    del students[chk]
                    print("{} 학생 성적이 삭제되었습니다. ".format(search))
                    print(students)
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("선택된 서비스가 없습니다.")
                
                     

                
            
            
        
                
        
            

        