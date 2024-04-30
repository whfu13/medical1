-- employees 테이블에서 
-- 사번,이름,월급,실제월급(월급+(월급*커미션)),월급*1410 원화로 환산해서
-- 원화표시, 천단위 표시해서 출력하시오.

select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),
to_char(salary*1410,'999,999,999') as kor_salary 
from employees
order by employee_id;

select * from employees;
select department_id, round(avg(salary),2),max(salary),min(salary) 
from employees
where department_id is not null
group by department_id
order by department_id;

select * from stu_score
order by no;

select * from stu_score
where name like '%홍%'
;

select * from stu_score
where avg >= 60
order by no
;

-- equl join
-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오.
select employee_id, emp_name,a.department_id, department_name
from employees a,departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary>=(select avg(salary) from employees)
;

-- 그리고, 이름 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%'
;

-- 월급이 평균이상인 사람만 검색하시오.
select salary from employees
where salary>=(select avg(salary) from employees)
and salary>=(select avg(salary) from employees)
;

select * from employees;

select * from jobs;

-- 사원번호,사원명,부서번호,부서명,직급번호,직급명
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title
from employees a,departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id
;
-- 사원번호, 사원명, 월급, 최소월급분, 인상분, 직급,직급타이틀 출력하시오.
select employee_id, emp_name, salary, min_salary, a.job_id, job_title 
from employees a, jobs b
where a.job_id = b.job_id
;
-- 사원번호, 사원명, 월급, 최소월급분, 인상분, 직급,직급타이틀 출력하시오.
-- 최소월급 몇% 이상을 받고 있는지 출력(최소월급 / 현재월급 * 100)
select employee_id, emp_name, salary, min_salary,to_char(round(((salary-min_salary)/salary)*100,2))||'%',a.job_id, job_title 
from employees a, jobs b
where a.job_id = b.job_id
;

-- job_title Manager 글자가 들어가 있는
-- 사원번호, 사원명, 직급번호, 직급명, 월급, 최대월급을 출력하시오.
select employee_id, emp_name, a.job_id, job_title, salary, max_salary
from employees a, jobs b
where a.job_id = b.job_id and job_title like '%Manager%' 
;

select user_id,user_name,user_phone,user_address1,user_address2,user_address3
from User a, Deliver_address b
where a.user_id = b.user_id
;

create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'F',50,59
);

commit;

select * from stu_grade;

select * from stu_score;

-- case when then grade컬럼을 만들어 90이상 A, 80점 B
select no,name,avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score
order by no
;

-- Non-equi join
select no,name,avg,grade
from stu_score,stu_grade
where avg between low_score and high_score
order by no;
-- stu_score,stu_grade 같은 컬럼이 없음.
-- 2개 테이블을 join : non-equl join
select * from stu_score;
select * from stu_grade;

update stu_grade set low_score=0
where grade = 'F'
;

commit;

-- 월별매출액을 기준으로 고객등급
-- 지역별 대출합계를 출력하시오.
select * from kor_loan_status;
select region,gubun,sum(loan_jan_amt) a
from kor_loan_status
group by region,gubun
order by a;

-- 년도별, 지역별, 대출합계금액
select substr(period,1,4),region,sum(loan_jan_amt)
from kor_loan_status
group by substr(period,1,4),region
order by region
;
-- 부서별 월급 합계를 출력하시오.
select department_id, sum(salary)a
from employees
group by department_id
order by a;

-- 시간대별,연령대별 판매량 총합을 출력하시오.
select * from lotte_product;
select time_cd,age_cd,sum(purh_amt)a
from lotte_product
group by time_cd,age_cd
order by a desc
;

select * from shop_product;

-- 이름별, 금액합계를 출력하시오.
select name, sum(amount) a
from shop_product
where pdate>='2024/03/01'
group by name
order by a
;

-- customer_rank 테이블 생성
-- rank
-- 100만원 이하 BRONZE
-- 200만원 미만 SILVER
-- 300만원 미만 GOLD
-- 300만원 이상 PLATINUM

-- name,sum(amount),rank 출력하시오.
-- non-equi join
create table customer_rank(
rank varchar2(10) primary key,
low_amount number,
high_amount number
);

insert into customer_rank values(
'PLATINUM',3000000,9999999
);

select name,s_amount,rank
from
(select name,sum(amount) s_amount
from shop_product
where pdate>='2024/03/01'
group by name
),customer_rank
where s_amount between low_amount and high_amount
;

-- Non-equi join
select no,name,avg,grade
from stu_score,stu_grade
where avg between low_score and high_score
order by no;

select * from lotte_product
order by std_ym
;

-- 순번을 새롭게 부여해서 출력해주는 함수
-- rownum, row_number()
select rownum,std_ym,sex_cd,time_cd,purh_amt
from lotte_product
;

select rownum,a.*
from lotte_product a
where rownum<=10;

select rownum,a.*
from
(
select rownum rnum,a.* from lotte_product a
) b
where rnum>=11 and rnum <=20;

select rownum,b.*
from ( select * from lotte_product order by std_ym) b
;

select * from stu_score
order by no
;

-- kor점수가 높은순으로 21~30등까지 출력하시오.
select rnum,no,name,kor,eng,math,total,avg,rank,c_date
from ( 
select rownum rnum,b.* from 
( select a.* from stu_score a
order by kor desc) b
) 
where rnum >=21 and rnum <=30
;


select * from stu_score;

select * from stu_score 
where no>=1 and no<=10
order by no;