
# 숫자 두개를 입력받고,
# 연산자를 입력받아서(+-*/)
# 무한히 계산하는 계산기를 만드는데
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요
while True: 
    n1 = int(input('첫번째 숫자를 입력하세요 >>'))
    n2 = int(input('두번째 숫자를 입력하세요 >>'))
    cal = input('수식을 입력하세요 >> ')
    if n1 == 0:
        break
    if cal == '+':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif cal == '-':
        print('{}-{}={}'.format(n1,n2,n1-n2))
    elif cal == '*':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif cal == '/':
        print('{}/{}={}'.format(n1,n2,n1/n2))
    else:
        print('잘못된 수식을 입력하셨습니다.')    

print('프로그램이 종료되었습니다.')