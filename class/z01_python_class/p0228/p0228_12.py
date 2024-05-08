# 1. 변수선언
score = [[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
name = ['홍길동','유관순','이순신','김구']
total = []
# 2. 코딩
# 2 -1) 요소 하나하나 출력 80 90 85 70 80 90 ...
for i in range(len(score)):
    # print(score[i])
    for j in range(len(score[i])):
        print(score[i][j])          
# 2 -2) 작은 요소의 합을 구해서 total 넣어주세요
#       total = [255,240,c,d]
sum = 0
for i in range(len(score)):
    for j in range(len(score[i])):
        sum = sum + score[i][j]
total.append(sum)

# 3. 출력
# 3 - 1) total = [255,240,256,229]
print(total)
    

# 3 - 2) 250 미만 불합격 250 이상 합격 ex) 홍길동님 합격입니다 출력
for i in range(4):
    if total[i] >= 250:
        print('{}님 합격입니다.'.format(name[i]))
    else: 
        print('{}님 불합격입니다.'.format(name[i]))