# 두수를 입력받아, 두수 사이의 합계를 구하시오.

# 1. 두수 입력
# 2. 함수 호출
# 3. 1,10 # 1+2+3+4...10
# 4. 합계를 리턴받아서
# 5. 합계: 55 출력

# 1-10까지의 더하기,빼기,곱하기의 결과를 출력하시오.


def cal(s_list):
    for i in range(s_list[0],s_list[1]+1):
        s_list[2] += i 
        s_list[3] -= i
        s_list[4] *= i


num1 = int(input("1번째 숫자를 입력하세요. >>"))
num2 = int(input("2번째 숫자를 입력하세요. >>"))
s_list = [num1,num2,0,0,1]
cal(s_list)

print("더하기 결과값 : ",s_list[2])
print("빼기 결과값 : ",s_list[3])
print("곱하기 결과값 : ",s_list[4])
    