import datetime # 날짜 관련 기능을 가져옴
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴
year = now.year

# 시간을 사용해서
# 지금이 오전이면 오전입니다. 오후면 오후입니다 출력
h = now.hour # 시간
# 오전
if h < 12 :
    print('현재는 {}시로 오전입니다.'.format(h))
else:
    print('현재는 {}시로 오후입니다.'.format(h))
# [현재는 17시로 오후입니다.]
print(now) # => 2024-02-22 17:07:56.690958

print(now.year) # 연도
print(now.month) # 월
print(now.day) # 일

print(now.hour)
print(now.minute)
print(now.second)
