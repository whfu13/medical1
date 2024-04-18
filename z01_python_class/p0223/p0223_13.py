
# 빈 리스트 생성
cont = []
print('방법1 : ', cont)
c1 = input('1.나라를 입력해주세요 >> ')
c2 = input('2.나라를 입력해주세요 >> ')
c3 = input('3.나라를 입력해주세요 >> ')
c4 = input('4.나라를 입력해주세요 >> ')
cont = [c1,c2,c3,c4]

# [미국, 영국, 일본, 중국]
# cont.append(변수)

print(cont)
contA = []
contA.append(c1)
contA.append(c2)
contA.append(c3)
contA.append(c4)

print('방법2',contA)


cont = ['미국', '영국', '일본', '중국']
print('{}-{}-{}-{}'.format(c1,c2,c3,c4))
# cont = [c1,c2,c3,c4]
# contA = [] <= append로 채움
print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[3]))

f = [] # 과일리스트
# 내가 입력한 과일들로 리스트를 채워보세요 과일 3개이상
print(f[0])



a= input('종아하는 과일을 입력하세요 >> ')
b= input('종아하는 과일을 입력하세요 >> ')
c= input('종아하는 과일을 입력하세요 >> ')

f.append(a)
f.append(b)
f.append(c)