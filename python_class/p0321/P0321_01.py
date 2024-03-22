class Student:
    name = ""
    kor = 0
    
    def __init__(self,name=""):
        pass
    def stu_print(self):
        print("학생성적을 출력합니다.")
        
def s_print():
    print("class 밖에 있는 함수")

s = Student() # 객체선언할때 무조건 init() 함수 호출
print(s)

s_print()
s_print()
s_print()
class Lotto():
    pass
s2 = Lotto()

s.stu_print() # 클래스 내에 있는 함수는 꼭 객체선언을 해야 사용가능

if isinstance(s2,Student):
    print("Student 클래스 변수입니다.")
elif isinstance(s2,Lotto):
    print("Lotto 클래스 변수입니다.")
    
print(type(s2))