import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성

# board 정보에서 id,name 포함해서 데이터를 가져와 출력하시오.
# board 테이블 id 포함 모든 컬럼, member 테이블의 name 컬럼을 가져와 출력하시오.
# board 테이블 id, member 테이블 name
# sql = "select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile \
# from board a, member b \
# where a.id = b.id"

# stu_score avg 90점 이상 A, 80 이상 B,C,D, 60점 미만 F
# 학번,이름,합계,평균,학점 출력하시오.
# sql = "select no,name,total,avg,\
#     case\
#     when avg>=90 then 'A'\
#     when avg>=80 then 'B'\
#     when avg>=70 then 'C'\
#     when avg>=60 then 'D'\
#     else 'F'\
#     end as grade\
#     from stu_score"

sql = "select * from stu_score"
# sql구문을 통해 가져온 데이터 중
# 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오.
# 학번,이름,합계,평균,학점
cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall() # fetchall(): 모든 데이터 가져옴. fetchone(): 1개의 데이터 가져옴.
print("[ 모든 데이터 출력 ]")
# print(data)
for d in data:
    print(d)
    no = d[0]
    name = d[1]
    total = d[5]
    avg = d[6]
    if avg>=90:
        grade = "A"
    elif avg>=80:
        grade = "B"
    elif avg>=70:
        grade = "C"
    elif avg>=60:
        grade = "D"
    else:
        grade = "F"
    print("학번 : ",d[0])
    print("이름 : ",d[1])
    print("합계 : ",d[5])
    print("평균 : ",d[6])
    print("학점 : ",grade)
    print("-"*20)
print("-")
print("타입 : ",type(data))


# salary 평균을 출력하시오.

sql = "select round(avg(salary),2) as salary from employees"
cursor.execute(sql)
date = cursor.fetchone() # 데이터 결과값이 1개일때
print(data[0])
conn.close() # 데이터베이스 연결해제