member = []
cnt = 0
# 이름을 입력을 받아서 [[1, 홍길동],[2, 유관순],[3, 이순신]]
while True:
    print('-'*25)
    print('1.입력')
    print('2.전체출력')
    print('3.검색출력')
    print('4.검색삭제')
    print('0.종료')
    ch = input('원하는 번호를 선택하세요 >> ')
    print('-'*25)
    if ch.isdigit():
        ch = int(ch)
    if ch == 1:
        print('입력')
        name = input('이름을 입력해주세요 >> ')
        cnt = cnt+1
        m = [cnt, name]
        member.append(m)
    elif ch == 2 :
        # print('출력')
        print('번호\t이름')
        print('-'*20)
        for i in range(len(member)):
            print('{}\t{}'.format(member[i][0],member[i][1]))
            
    elif ch == 3 : # 3. 검색출력
        searName = input('검색하고 싶은 학생의 이름을 입력해주세요 >>')
        print('번호\t이름')
        for i,m in enumerate(member): # m = [1,홍길동] , [2, 유관순]...
            if searName in m:
                print('{}\t{}'.format(member[i][0],member[i][1]))
                
    
    elif ch == 4: # 4. 검색삭제
        delNmae = input('삭제하고 싶은 학생의 이름을 입력해주세요 >> ')
        
        for i,m in enumerate(member):
            if delNmae in m:
                del(member[i])
                print('삭제되었습니다.'.format(delNmae))
    elif ch == 0 :
        print('종료')
        break
    elif ch == 5:
        print('수정')
        reName = input('수정하고 싶은 학생의 이름을 입력해주세요 >>')
        
        for i, m in enumerate(member): # m = [1,홍길동], [2,유관순]...
            if reName in m: # 존재한다면
                print(reName, '님을 선택하셨습니다.')
                ch_num = input('수정하고 싶은 항목을 선택해주세요(1.번호수정),2.이름수정)')
                if ch_num == '1':
                    print(reName,'님의 번호 수정을 선택하셨습니다')
                    print(reName,'님의 번호는',member[i][0],'입니다')
                    # 수정하는 코드 입력을 받아서, 수정하기
                    stu_num = input('새로운 번호를 입력해주세요 >>')
                    stu_num = int(stu_num)
                    member[i][0] = stu_num
                elif ch_num == '2':
                    print(reName,'님의 이름 수정을 선택하셨습니다')
                    print(reName,'님의 이름은',member[i][1],'입니다')
                    stu_name = input('새로운 이름을 입력해주세요 >>')
                    member[i][1] = stu_name
                else:
                    print('잘못입력하셨습니다.')
                    break
    else:
        print('다시입력')