-- 테이블 조회 
select * from post;
select * from users;
select * from member2;

-- 게시물 테이블 --
create table post(
post_no number(4) primary key, 
user_id varchar2(30),
post_title varchar2(1000),
post_content clob,  
post_group number,
post_step number default 0,
post_indent number default 0,
post_hit number default 0,
post_reg_date date default sysdate,
post_file varchar2(100),
constraint fk_user
foreign key(user_id)
references users(user_id) -- 사용자 테이블 참조 외래키
);

-- 컬럼 부분 삭제
delete post where post_no=19;

-- 값 수정
alter table post modify post_title not null;

-- 데이터값 추가
insert into post(post_no,user_id,post_title,post_content,post_group,post_step,post_indent,post_hit,post_reg_date,post_file)values(
post_seq.nextval,'aaa','테스트1','내용1',post_seq.currval,0,0,0,sysdate,'null'
);

insert into post(post_no,user_id,post_title,post_content,post_group,post_step,post_indent,post_hit,post_reg_date,post_file) values (
post_seq.nextval,'bbb','테스트2','내용2',post_seq.currval,0,0,0,sysdate,'null'
);

-- 값 수정
update post
set post_file = 'file2.txt'
where user_id = 'bbb';

-- 값 삭제
drop table post;

-- 컬럼 데이터 타입, 길이 변경
alter table users modify temppw varchar2(255);

-- 컬럼 명 변경
alter table users rename column user_reg_date to mdate;

-- 컬럼 추가
alter table users add phone varchar(20) not null;

alter table users add gender varchar(10) not null;

alter table users add hobby varchar(200) not null;

alter table users add auto_login_token varchar(20) not null;

alter table users add temppw varchar(20) not null;

insert into users(user_id,user_name,user_pw,user_email,user_reg_date) values(
'aaa','홍길동','1111','wawd@naver.com',sysdate
);

insert into users(user_id,user_name,user_pw,user_email,user_reg_date) values(
'bbb','유관순','2222','dasd@naver.com',sysdate
);

insert into users(user_id,user_name,user_pw,user_email,user_reg_date) values(
'ccc','이순신','3333','abasd@naver.com',sysdate
);

commit;