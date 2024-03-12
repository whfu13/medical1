def stu_update(student): # 지역변수 => 주소값이 저장
    student["stuNo"] = 2
    student["name"] = "유관순"
    student["total"] = student["kor"]+student["eng"]+student["math"]
    student["avg"] = student["total"]/3
    



# 프로그램 구현
student = {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33} # 2개의 이상의 변수

# 함수호출
stu_update(student) # 전역변수

print("학생1 : ",student)