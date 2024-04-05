season = input("월을 입력하세요")
month1 = season[0:-1]
month = int(month1)

if 3<=season<=5:
    print("봄")
elif 6<=season<=8:
    print("여름")
elif 9<=season<=11:
    print("가을")
else:
    print("겨울")