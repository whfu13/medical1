 1` 
 -- 테이블 생성
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

desc emp01;

-- 테이블생성:  테이블 구조 및 데이터 모두 복사
create table emp02 as
select * from employees;

-- 테이블 구조만 복사하기
create table emp03 as
select * from employees where 1=2;

-- 테이블이 구조가 다르면서, 데이터를 복사하기( 3개 => 14개 )
insert into emp01(emp_id,emp_name,hire_date)
select employee_id,emp_name,hire_date from employees;

-- 1개 데이터 추가
insert into emp01 values (
207,'홍길동','2024-04-26'
);

-- 테이블이 구조가 같으면서 데이터만 복사 ( 구조가 같은 경우 )
insert into emp03
select * from employees;

select * from emp01;
select * from employees;
select * from emp01 order by emp_id desc;
select * from emp03;

-- 컬럼 타입변경
alter table member
modify(stu_name varchar2(30));

-- 컬럼 삭제
alter table member
drop column pw;

-- 컬럼 추가
alter table member
add (pw varchar2(30));

select * from member;

select mno,id,pw,stu_name,gender from member;
select * from member;

insert into member values (
seq_mno.nextval,'ggg','1111','홍길자','male'
);

-- 컬럼 순서 변경
-- 컬럼 숨기기
alter table member modify stu_name invisible;
alter table member modify gender invisible;
-- 컬럼 보여주기
alter table member modify stu_name visible;
alter table member modify gender visible;

select * from member;

-- 컬럼 일시적 사용 제한
alter table member
set unused(id);

-- 사용 제한 해제
alter table member
drop unused columns;

-- 테이블 삭제
-- drop table s_info;
-- drop table m_date;
drop table emp03;

-- 테이블 이름 변경
rename emp01 to employees01;
select * from employees01;

desc employees;

-- [ 무결성 제약조건 ]
-- foreign key는 다른 테이블에서 데이터 입력시 
-- 선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인

-- drop table employees01;
-- drop table emp02;
-- drop table member;
-- drop table board;

create table member (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','홍길동','male'
);

insert into member(id,pw,name) values(
'bbb','1111','유관순'
);
insert into member(id,pw) values(
'ccc','1111'
);

insert into member(id,pw,name) values(
'a','1111','홍길동'
);
select * from member;

-- 제약조건: not null - null값은 제외
create table emp02 (
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

-- 제약조건: unique - 중복만 제거, null허용
create table emp01 (
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

insert into emp01 values (
5,'홍길자','0005',5
);

select * from emp01;

select * from emp03
where empno=1;

select * from emp03
where empno is null and ename='홍길동';

-- foreign key (외래키)
-- drop table emp01;

-- emp01 테이블 생성
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(6)
);


alter table emp01
modify(deptno number(6));
;

select * from emp01;

commit;

-- emp01 foreign key 추가
-- fk_deptno: 별칭
-- add constraint 별칭 foreign key(현재 컬럼), references 다른 테이블(컬럼이름)
alter table emp01
add constraint fk_deptno foreign key(deptno)
references dept01(deptno)
;


insert into emp01 values(
5,'강감찬','0004',1
);

-- foreign key 삭제
alter table emp01
drop constraint fk_deptno;


-- dept01 테이블 생성
create table dept01(
deptno number(6) primary key,
dept_name varchar2(20)
);

insert into dept01(deptno,dept_name)
select department_id,department_name from departments;

desc departments;
alter table dept01
modify( deptno number(6));

select * from departments;

create table board (
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(
8,'bbb','게시글8','내용8'
);

commit;

select * from board;

alter table board
add constraint fk_id foreign key (id)
references member(id);

-- comment 테이블 댓글테이블

-- cno number(4) primary key
-- bno number(4)
-- cpw varchar2(20)
-- ccontent varchar2(1000)

create table comments(
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno)
references board(bno)
);

-- 댓글 달기
insert into comments values(
5,5,'1111','댓글내용5'
);

-- fk를 등록할때 설정 
-- fk키로 등록되어 있는 모든 데이터를 삭제시키는 것.
-- fk키로 등록되어 있는 데이터는 모두 존재시키는 것.
delete board where bno=5;

commit;

select * from comments;
select * from board;

-- 외래키 삭제
alter table board drop constraints fk_id;
alter table comments drop constraints fk_bno;


select * from board;
select * from comments;

delete board where bno=1;

alter table board
add constraint fk_id foreign key (id)
references member(id);

-- fk_cno 삭제가 되도록 함.
alter table comments
add constraint fk_bno foreign key(bno)
references comments(bno) on delete cascade;

alter table board add foreign key(bno)
delete comments where cno=2;

-- check 제약조건 특정값의 범위, 특정값만 입력되도록 함.
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', -- 컬럼에 데이터를 넣지 않으면 자동으로 0001이 저장됨.
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in('남자','여자'))
);

insert into emp(empno,ename,job,sal,gender) values(
6,'김유신','0001',20000,'남자'
);

-- 에러: '남자,여자'만 가능
insert into emp(empno,ename,job,sal,gender) values(
3,'이순신','0004',5000,'남'
);

-- 에러: 2000~20000 사이만 가능
insert into emp(empno,ename,job,sal,gender) values(
3,'이순신','0004',5000,'남자'
);

-- job
insert into emp(empno,ename,sal,gender) values(
3,'이순신',5000,'남자'
);

select * from emp