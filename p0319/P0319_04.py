# student클래스 생성, 파일불러와서 클래스에 저장후 출력하시오.
class Student:
    
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
        return f"학생성적 : {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"

students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "":break
    txt_list = txt.split(",")
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
    
f.close()

# 파일 불러오기 한후 학생수에서 +1추가
Student.count = len(students)+1
# for stu in students:
#     print(stu)
    
# 학생성적 화면 함수
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
    print('7. 학생성적 파일저장')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    
    cnt = 0

    if choice == "1":
        while True:
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
            if(name=="0"):
                print("학생 입력을 취소합니다.")
                break
            kor = int(input("국어 점수를 입력하세요 >> "))
            eng = int(input("영어 점수를 입력하세요 >> "))
            math = int(input("수학 점수를 입력하세요 >> "))
            s = Student(name,kor,eng,math)
            students.append(s)
            print("입력 데이터 : ",s)
        
        
    elif choice == "2":
        count = input("학생전체 출력을 하시겠습니까? (1.확인, 0.취소)")
        if count == "0":
            break
        print('\t[ 학생성적전체출력 ]')
        print('-'*65)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        print('-'*65)
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end="\t")
            print()
        print("-"*65)
        print()