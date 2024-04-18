-- 가지고 있는 테이블 검색
select * from tab;

select * from employees;

-- 테이블 구조확인
desc employees;

-- 테이블 생성
create table stu_score (
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2)
);

insert into stu_score(no,kor,eng,avg) values (
1,100,99,(100+99)/2
);

insert into stu_score values (
1,95,98,(95+98)/2
);

insert into stu_score values (
    1,80,70.223,(80+70.223)/2
);

select * from stu_score;

commit;

create table num (
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);

-- 현재날짜 : 년/월/일 기본형태
-- dual : 가상테이블
select sysdate from dual;

-- 날짜 포맷 변경 : to_char 형변환 => 포맷을 지정
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

select to_char(sysdate,'hh:mi:ss') from dual;

select sysdate+2000 from dual;

select sysdate - to_date('24-01-01') from dual;

