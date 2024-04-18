students = [[1, "홍길동",90,100,99,289,99.97,1],
            [2, "유관순",80,100,99,279,99.97,1],
            [3, "이순신",100,100,99,299,99.97,1],
            [4, "김구",100,100,90,290,96.67,1],
            [5, "김유신",90,70,50,210,70.0,1]]

while True:
    search = input("삭제하려는 학생의 이름을 입력하세요.")
    
    # 이름찾기
    cnt = 0 # 찾은 학생의 위치
    # 전체 학생 검색
    for stu in students:
        if stu[1] == search:
            break
        cnt += 1
        
        if cnt == len(students): # 전체학생수
            print("{} 학생이 없습니다.".format(search))
        else:
            print("{} 학생을 찾았습니다.".format(search))
        print("찾은위치 : ",cnt)
        del students[cnt]
        print(students)
    print("-"*40)
        