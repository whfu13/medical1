print("1234".isdigit()) # 숫자로 취환가능한지 확인 >>>>>>> (중요)
print("1234a".isdigit()) # 숫자인지 확인
print("abc".isalpha()) # 영문으로 취환가능한지 확인 >>>>>>(중요)
print("a1bc".isalpha()) # 영문인지 확인
print("abc".islower()) # 소문자인지 확인
print("abcD".islower()) # 소문자인지 확인
print("ABC".isupper()) # 대문자인지 확인
print("ABaC".isupper()) # 대문자인지 확인
print(" ".isspace()) # 문자열이 공백인지 확인 >>>>>> (중요)
print(" ab c".isspace()) # 빈공백이 있는지 확인