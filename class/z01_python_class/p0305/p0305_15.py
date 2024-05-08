import operator

numbers = ['바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1
        
print(dict(sorted(counter.items(),key=operator.itemgetter(0),reverse=True)))

print(counter)