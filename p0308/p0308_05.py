import random

card_list = [['spade', 2], ['diamond', 5], ['heart', 8], ['diamond', 'A'], ['spade', 10], 
 ['diamond', 'K'], ['clover', 4], ['spade', 5], ['heart', 'Q'], ['diamond', 2], 
 ['diamond', 4], ['heart', 7], ['clover', 'A'], ['diamond', 7], ['heart', 'A'],
 ['spade', 6], ['diamond', 6], ['clover', 8], ['spade', 8], ['heart', 'J'], 
 ['diamond', 'J'], ['diamond', 'Q'], ['clover', 7], ['spade', 9], ['spade', 3], 
 ['heart', 4], ['clover',10], ['clover', 5], ['spade', 7], ['spade', 'J'], 
 ['spade', 'A'], ['heart', 6], ['diamond', 8], ['heart', 2], ['heart', 5], 
 ['diamond', 9], ['diamond', 3], ['heart',3], ['clover', 9], ['clover', 'Q'],
 ['clover', 2], ['heart', 'K'], ['diamond', 10], ['spade', 'K'], ['spade', 'Q'], 
 ['clover', 3], ['spade', 4],['heart', 9], ['clover', 'K'], ['clover', 6], 
 ['heart', 10], ['clover', 'J']]

arr_num = 0
while True:
    print("[ 카드 게임 ]")
    print("-"*30)
    print("1. 카드1장 뽑기")
    print("2. 카드5장 뽑기")
    print("0. 종료")
    print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]))
    c_num = int(input("번호를 선택해주세요. "))
    
    if c_num == 1:
        print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]))
        arr_num += 1
    elif c_num == 2:
        for i in range(5):
            print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]))
            print()
            arr_num += 1
        