select * from board order by bgroup desc, bstep asc;

-- 리스트 호출시
select rownum, a.* from (select * from board order by bgroup desc, bstep asc) a
where rownum>=1 and rownum<=10
;

-- 검색 호출시
select rownum, a.* from (select * from board order by bgroup desc, bstep asc) a
where rownum>=1 and rownum<=10
and btitle like '%사진%' or bcontent like '%사진%'
;

select * from
(select rownum rnum, a.* from (select * from board order by bgroup desc, bstep asc) a)
where rnum>=11 and rnum<=20
;
select * from
(select row_number()over(order by bgroup desc, bstep asc) rnum, a.* from board a)
where rnum>=11 and rnum<=20
;

-- rnum로 찾기
select rnum from
(select row_number()over(order by bgroup desc, bstep asc) rnum, a.* from board a)
where bno = 31;

-- 현재글
select * from
(select row_number()over(order by bgroup desc, bstep asc) rnum, a.* from board a)
where rnum = (
select rnum from
(select row_number()over(order by bgroup desc, bstep asc) rnum, a.* from board a)
where bno = 33
)+1
;

-- 이전글
select * from
(select row_number()over(order by bgroup desc, bstep asc) rnum, a.* from board a)
where rnum = 12+1;

-- 다음글
select * from
(select row_number()over(order by bgroup desc, bstep asc) rnum, a.* from board a)
where rnum = 12-1;

select * from board 
where btitle like '%뉴진스%'
order by bgroup desc, bstep asc
;

-- 게시글 총 개수
select count(*) from board
;

select count(*) from board
where btitle like '%사진%' or bcontent like '%사진%'