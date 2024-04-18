import random

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER  4종류
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K    13장
# 카드 총 수 : 52장

# 카드 생성
def card_creat():
    pass

# 카드 섞기
def card_shuffle():
    pass

# 카드 나눠주기
def card_share():
    pass

# 카드 확인하기
def card_print():
    pass

while True:
    print("[ 카드 프로그램 ]")
    print("1. 카드생성")
    print("2. 카드섞기")
    print("3. 카드5장 나눠주기")
    print("4. 카드5장 확인하기")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    shape_list = ["SPADE", "DIAMOND", "HEART", "CLOVER"]
    num_list = [0]*13
    card_list = [[0]*2 for i in range(52)]
    cnt = 0
    if choice == 1:
        for i in shape_list:
            for j in range(13):
                card_list[cnt] = {"shape":i,"num":num_list[j]}
                cnt += 1
            
        card_creat()
        
    elif choice == 2:
        random.shuffle(card_list)
        card_shuffle()

    elif choice == 3:
        card_share()

    elif choice == 4:
        card_print()
        
    else:
        print("프로그램을 종료합니다.")
        break
