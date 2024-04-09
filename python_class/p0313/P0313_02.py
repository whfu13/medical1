def cal(num1,num2):
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1+num2
    r_list[3] = num1-num2
    r_list[4] = num1*num2
    r_list[5] = num1/num2
    return r_list

save_list = []


while True:
    # 두수입력을 받아 값을 리턴 받은 다음, 출력하시오.
    # print("1.더하기 2.빼기 3.곱하기 4.나누기")
    num1 = int(input("1번째 숫자를 입력하세요 >> (0.종료)"))
    if num1 == 0:
        break
    num2 = int(input("2번째 숫자를 입력하세요 >> "))
    # c = input("원하는 사칙연산을 입력하세요.")

    r_list = cal(num1,num2)
    # save_list에 r_list를 저장
    save_list.append(r_list)

    # list일경우 *list = list[0],list[1],list[2],list[3]
    print("{},{}결과값 : {},{},{},{} ".format(*r_list))

# 현재까지 입력한 숫자와 결과값을 모두 출력해보세요.
    print("[ 현재까지 입력한 숫자, 결과값 ]")
# 10,20 결과값 : 30,-10,200,0.5
for s in save_list:
    print("{},{}결과값 : {},{},{},{} ".format(*s))