# 입력 : 이름, 아이디, 비밀번호 (input)
# 5명을 입력받아서 member 리스트를 만드세요

member = [] # [[홍길동], aaa, 111],[유관순,bbb,111]]

'''
member리스트를
이름    아이디  비밀번호
홍길동  aaa     1111
이순신  bbb     2222

형식으로 출력해보세요

'''
name = []

for i in range(5):
    n1 = input('이름을 입력하세요 >> ')
    ag = input('나이를 입력하세요 >> ')
    name.append(n1)
    p = [n1, ag]
    member.append(p)
    
print(name)

for i in range(5):
    name = input('이름을 입력하세요 >> ')
    id = input('아이디를 입력하세요 >> ')
    pw = input('패스워드를 입력하세요 >> ')
    p= [name,id,pw]
    member.append[p]
# member 리스트를 사용해서 출력
a = len(member) # 5
print('이름\t아이디\t비밀번호\t')
for i in range(len(member)) : # i 0 1 2 3 4
    print('{}\t{}\t{}\t'.format(member[i][0],member[i][1],member[i][2]))
    