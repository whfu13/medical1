member = []

# 입력: 이름,점수 (input) ['홍길동, 90]
# 총 3명의 정보를 member 리스트에 넣으세요

print(member) # [['홍길동',90],['유관순',91],['이순신',95]]

name = []

for i in range(3):
    n1 = input('이름을 입력하세요 >> ')
    s1 = int(input('점수를 입력하세요 >> '))
    name.append(n1)
    p = [n1,s1]
    member.append(p)    
    
a = len(member)
print('이름\t점수\t')
for i in range(len(member)):
    print('{}\t{}\t'.format(member[i][0],member[i][1],member[i][2]))

member = [['홍길동',55],['유관순',80],['이순신',90]]   
print(member) # [['홍길동',90],['유관순',91],['이순신',95]]

# 60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다
# member 변수 사용, for, if

for i in range(len(member)):
    name = member[i][0]
    s1 = member [i][1]
    if s1 >= 60:
        print('{}님 합격입니다.'.format(name))
    else:
        print('{}님 불합격입니다.'.format(name))
    