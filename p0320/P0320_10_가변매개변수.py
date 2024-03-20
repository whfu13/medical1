print(range(10))
a = range(10)
print(a)

print(list(range(10))) 
print([ i for i in range(10)])

# 키워드 변수는 항상 맨뒤, 가변 매개변수는 맨앞쪽 x
# 기본-가변-키워드 순으로 
def func(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
    print()

func("안녕하세요","즐거운","파이썬 프로그래밍",n=3)