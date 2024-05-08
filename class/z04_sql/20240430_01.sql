select a.*,name from board a,member b
where a.id = b.id
;

select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile
from board a, member b
where a.id = b.id
;

select * from stu_score;

select no,name,total,name,avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score;

select * from employees;

select round(avg(salary),2) as salary from employees;

