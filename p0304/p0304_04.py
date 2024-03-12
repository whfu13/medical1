students = [["홍길동",90,100,99,299,99.97],
            ["유관순",80,100,99,299,99.97],
            ["이순신",100,100,99,299,99.97]]
kors = 0
for i,stu in enumerate(students):
    kors += stu[1]
    
print(kors)