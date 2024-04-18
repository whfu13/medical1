# 점수를 입력받아서
# 1. 90점 이상이면 A
# 2. 80점 이상이면 B
# 70점 이상이면 C 나머지는 F를 출력 (elif)

n = int(input("점수를 입력하세요 >>"))
if n >= 90 :
    print("A")
    if n >= 98:
        print("A+")
    elif n > 93:
        print("A")
    else:
        print("A-")             
elif n >= 80 :
    print("B")
    if n >= 88:
        print("B+")
    else:
        print("B-")    
    
elif n >= 70 :
    print("C")
    if n > 78:
        print("C+")
    else:
        print("C-")     
else:
    print("F")            


# 2. 98점 이상 A+ 90-93 사이는 A-
    
# B+, B-, C+, C- (중첩 if)   