import oracledb

# DB연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # 커서 생성: 명령어 입력받는 함수   

sql = "create table mem (id varchar2(30), pw varchar2(30) primary key, name varchar(30),mdate date )"
cursor.execute(sql)

## ddl 명령어는 commit이 없음. create,alter
## dml 명령어 : insert,update,delete

print("테이블 생성 완료")

# DB연결해제
cursor.close()
conn.close()
