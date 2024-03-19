# student클래스 생성, 파일불러와서 클래스에 저장후 출력하시오.
class Student:
    
    count = 1 # 클래스 변수사용
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = rank
    def __str__(self):
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

#----------------
# 파일 불러와서 저장하기
#----------------
students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "":break
    txt_list = txt.split(",")
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
    
f.close()

search_txt = [
                "",
                "찾고자 하는 학생 이름을 입력하세요 >>",
                "몇 점이상 검색하시겠습니까?>>",
                "몇 점이하 검색하시겠습니까?>>"
            ]

# 파일 불러오기 한후 학생수에서 +1추가
Student.count = len(students)+1
#----------------
# 함수부분
#----------------

# 학생성적화면 함수
def main_title_print():
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생성적수정')
    # print('5. 등수처리')
    # print('6. 학생삭제')
    # print('7. 학생성적 파일저장')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    choice = int(choice)
    return choice

# 학생성적상단출력 함수
def stu_main_print():
    print('\t[ 학생성적전체출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)

# 학생성적입력 함수
def stu_insert():
    while True:
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        if(name=="0"):
            print("학생 입력을 취소합니다.")
            break
        kor = int(input("국어 점수를 입력하세요 >> "))
        eng = int(input("영어 점수를 입력하세요 >> "))
        math = int(input("수학 점수를 입력하세요 >> "))
        # list에 추가
        s = Student(name,kor,eng,math)
        students.append(s)
        print("입력 데이터 : ",s)
        
def stu_print():
    stu_main_print()
        # 데이터 출력
    for i in students:
        print(i) # 객체를 출력
    print()
    
# 학생성적검색 함수
def search_title_print():
    print("\t[ 학생성적 검색 ]")
    print("-"*40)
    print("1. 학생이름으로 검색")
    print("2. 점수이상 검색")
    print("3. 점수이하 검색")
    print("0. 이전화면 이동")
    choice = int(input("원하는 번호를 입력하세요 >> "))
    return choice

def stu_search(choice):
    if choice == 1:
        search = input(search_txt[choice])
    else:
        search = int(input(search_txt[choice]))
    # 전체리스트에서 학생검색
    s_list = []
    for i in students:
        if choice == 1:
            if i.name.find(search) != 1:
                s_list.append(i)
        elif choice == 2:
            if i.total >= search:
                s_list.append(i)
        elif choice == 3:
            if i.total <= search:
                s_list.append(i)
                
    if len(s_list) != 0:
        stu_main_print()
        for i in s_list:
            print(i)
    else:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요. ")
#-------------------
# 메인 프로그램 시작
#-------------------

# for stu in students:
#     print(stu)
    
# 학생성적 화면 함수
while True:
    choice = main_title_print() # 메인화면
    
    # 프로그램
    if choice == 1: stu_insert()  # 학생성적입력
    elif choice == 2: stu_print() # 학생성적전체출력
    elif choice == 3:             # 학생검색
        while True:
            choice = search_title_print()
            if choice == 0:
                print("이전화면으로 이동합니다.")
                print()
                break
            # 학생검색 프로그램 부분
            stu_search(choice)
    elif choice == 4: # 학생성적수정
        
        # 1. 이름으로 학생을 검색
        # 2-1. 찾았으면 과목 선택
        # 2-1-1. 과목리스트 출력
        # 2-1-2. 국어선택
        # 2-1-3. 국어점수 출력 후 국어점수 입력
        # 2-1-4. 국어점수 변경후 이전화면 이동
       
       # 2-2. 못 찾았으면 다시 이전화면으로 나옴.     
            
        s_title = ["","국어","영어","수학"]
        while True:
            search = input("찾고자 하는 학생의 이름을 입력하세요 (0.취소) >> ")
            cht = 0
            if search == "0":
                break
        for stu in students: #5명이 있으면 5번반복
            if stu.name == search:
                break
            cht += 1
        
        
        if cht == len(students):
            print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")
        else:
            print("찾고자 하는 학생의 위치 :",cht)
            print(students[cht])
           
            print("[ 수정할 과목 선택 ]")
            print("-"*30)
            print("1.국어\t2.영어\t3.수학")
            s_input = int(input("수정할려는 과목을 선택하세요.( 0.취소 ) >> "))









            
            