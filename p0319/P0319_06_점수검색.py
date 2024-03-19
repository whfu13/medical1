stu = [
    ["홍길동",100],["유관순",98],["이순신",95],["김구",50],
    ["강감찬",99],["김유신",90],["홍길순",80],["홍길자",70],
]

# 이름으로 검색해서 홍이 들어가는 사람을 모두 검색해서 출력하시오.
# 이름으로 검색해서 신이 들어가는 사람을 모두 검색해서 출력하시오.

while True:
    print("[ 학생성적 검색 ]")
    print("1. 이름으로 검색")
    print("2. 점수 검색")
    choice = int(input("원하는 번호를 입력하세요>> "))
    
    if choice == 1:
        search = input("이름을 입력하세요 >> ")
        search_list = []
        cnt = 0
        for s in stu:
            # if n.find(search) != -1:
            if search in s[0]:
                search_list.append(cnt)
            cnt += 1
                        
        if len(search_list) == 0:
            print("찾는사람이 없습니다.")        
        else:
            print(f"{search} (으)로 검색된 사람 : ",end=" ")
            for i in search_list:
                print(stu[i][0],end=" ")
            print()
            print()
            
    # 80 => 80점 이상인 사람의 이름이 출력되도록 해보세요.
    elif choice == 2:
        score = int(input("몇 점 이상을 검색하시겠습니까? "))
        # search = input("이름을 입력하세요 >> ")
        search_list = []
        cnt = 0
        for s in stu:
            # if n.find(search) != -1:
            if s[1] >= score: # 검색어가 포함이 되어 있는지 확인
                search_list.append(cnt)
            cnt += 1
                        
        if len(search_list) == 0:
            print(f"{score}보다 큰 점수는 없습니다.")        
        else:
            print(f"[ {score}보다 큰 점수 ] ")
            for i in search_list:
                print(stu[i][0],":",stu[i][1])
            print()
            print()