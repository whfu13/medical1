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

--1. update ����
update student a set rank = (rank);

--2. rank() ����
(select no,rank() over(order by total desc) ranks from students) b;

--3. update ������ rank()������ no�÷����� ��, rank�÷��� �˻�
update student a set rank = (
select ranks from (students) b
where a.no = b.no
);

-- 4. students ���̺��� ranks�� �� �ִ� ���̺��� �־���.
update students a set rank = (
select ranks from ( select no,rank() over(order by total desc) ranks from students ) b
where a.no = b.no
);

-- ��������
select no,total,rank from students
order by total desc;

-- no ��������
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

--���� 1.
--�Ի��Ϸ� ��������, �÷� �����ȣ, �����, job_id-����,�Ի���,���� �÷��� ����Ͻÿ�.
select * from employees;

select employee_id, emp_name, job_id,hire_date,salary
from employees
order by hire_date desc;

-- ���� 2.
-- �޿��� ���� �޴� ��������� ����ϵ� ������ ������, ��������� ���������Ͻÿ�.
select salary,emp_name from employees
order by salary, emp_name desc;

-- �����Լ�
-- abs
select -10, abs(-10) from dual;

-- floor(�Ҽ��� ���� ���� �Լ�), round(�ݿø� �Լ�)
select 34.789, floor(34.789) as f,round(34.789) as r from dual;

-- round(���,�ڸ���) ex)round(34.178,2) 2�ڸ����� ǥ��
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;

select 34.5678, round(34.5678,-1) from dual;

-- trunc ������ �ڸ��� ���� ����
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

-- ceil �ø�
select ceil(34.123) from dual;

-- �������� �ϴ��� �����ؼ� ����Ͻÿ�.
select trunc(kor,-1) from students;
order by kor;

-- ����,����,���� �ϴ��� �����ؼ� ����,����,���� �հ踦 ����Ͻÿ�.
select trunc(kor,-1) ����,trunc(eng,-1)����, trunc(math,-1)����, (trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1) �հ� from students;

-- mod ������
select round(100/7,2) from dual;
select mod(10,7) from dual;

-- ������
select 10/7 from dual;

-- ����. �����ȣ�� ¦���ΰ��� ����Ͻÿ�.
-- ���̽� employee_id%2 = 0
select employee_id from employees;
where mod(employee_id,2)=0
;

-- ���� �й��� 3�� ����ΰ͸� ����Ͻÿ�. students���̺�
select no from students
where mod(no,3)=0;

-- ������
create sequence seq_no
increment by 1  -- ���� 1�� ��.
start with 1    -- ������ 1���� ����
minvalue 1      -- �ּҰ� 1
maxvalue 9999   -- �ִ밪 9999
nocycle         -- ��ȯ���� ����
nocache ;       -- ĳ�� ������� ����

-- nextval ������ ��ȣ 1�� ����
select seq_no.nextval from dual;

-- currval ������ ��ȣ Ȯ��
select seq_no.currval from dual;
