create table students;
select * from students;

select * from students
order by name asc;

alter table students add rank number(3);

select * from students;

update students set rank=0;

commit;

select * from students;

select total, rank() over(order by total desc) rank
from students;

update students set total=0;

select * from students;

update students set total=(kor+eng+math);

--1. update 구문
update student a set rank = (rank);

--2. rank() 구문
(select no,rank() over(order by total desc) ranks from students) b;

--3. update 구문과 rank()구문을 no컬럼으로 비교, rank컬럼을 검색
update student a set rank = (
select ranks from (students) b
where a.no = b.no
);

-- 4. students 테이블에서 ranks가 들어가 있는 테이블을 넣어줌.
update students a set rank = (
select ranks from ( select no,rank() over(order by total desc) ranks from students ) b
where a.no = b.no
);

-- 역순정렬
select no,total,rank from students
order by total desc;

-- no 순차정렬
select no,total,rank from students
order by no;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

select max(hire_date)-min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

--퀴즈 1.
--입사일로 오름차순, 컬럼 사원번호, 사원명, job_id-직급,입사일,월급 컬럼을 출력하시오.
select * from employees;

select employee_id, emp_name, job_id,hire_date,salary
from employees
order by hire_date desc;

-- 퀴즈 2.
-- 급여를 적게 받는 사람순으로 출력하되 월급이 같으면, 사원명으로 역순정렬하시오.
select salary,emp_name from employees
order by salary, emp_name desc;

-- 숫자함수
-- abs
select -10, abs(-10) from dual;

-- floor(소수점 이하 버림 함수), round(반올림 함수)
select 34.789, floor(34.789) as f,round(34.789) as r from dual;

-- round(대상,자리수) ex)round(34.178,2) 2자리까지 표시
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;

select 34.5678, round(34.5678,-1) from dual;

-- trunc 지정한 자리수 이하 버림
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

-- ceil 올림
select ceil(34.123) from dual;

-- 국어점수 일단위 절사해서 출력하시오.
select trunc(kor,-1) from students;
order by kor;

-- 국어,영어,수학 일단위 절사해서 국어,영어,수학 합계를 출력하시오.
select trunc(kor,-1) 국어,trunc(eng,-1)영어, trunc(math,-1)수학, (trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1) 합계 from students;

-- mod 나머지
select round(100/7,2) from dual;
select mod(10,7) from dual;

-- 나누기
select 10/7 from dual;

-- 퀴즈. 사원번호가 짝수인것을 출력하시오.
-- 파이썬 employee_id%2 = 0
select employee_id from employees;
where mod(employee_id,2)=0
;

-- 퀴즈 학번이 3의 배수인것만 출력하시오. students테이블
select no from students
where mod(no,3)=0;

-- 시퀀스
create sequence seq_no
increment by 1  -- 증감 1씩 됨.
start with 1    -- 시작이 1부터 진행
minvalue 1      -- 최소값 1
maxvalue 9999   -- 최대값 9999
nocycle         -- 순환하지 않음
nocache ;       -- 캐시 사용하지 않음

-- nextval 시퀀스 번호 1씩 증가
select seq_no.nextval from dual;

-- currval 시퀀스 번호 확인
select seq_no.currval from dual;
