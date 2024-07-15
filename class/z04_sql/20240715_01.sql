select * from employees;

select * from departments;

-- join 사용: department_name까지 출력
select employee_id,emp_name,department_id,job_id,salary from employees;

select employee_id,emp_name,hire_date,salary,a.department_id,department_name,parent_id
from employees a, departments b
where a.department_id = b.department_id;

select * from employees a, departments b
where a.department_id = b.department_id
;

select * from board
order by bgroup desc, bstep asc;

create table commentB(
cno number primary key,
bno number(4),
id varchar2(30),
cpw varchar2(30),
ccontent varchar2(2000),
cdate date default sysdate
)
;

select * from board
where


-- foreign key 등록할려면 primary key로 등록이 되어 있어야 추가 가능
alter table commentB
add constraint fk_board_id
foreign key(id) references member2(id); 

alter table commentB
add constraint fk_board_bno
foreign key(bno) references board(bno); 

insert into commentB values(
commentb_seq.nextval,47,'ccc','','이벤트 신청합니다.',sysdate
)
;