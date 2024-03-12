aa = [[1,[3,4,5],3,4],[5,6],[7,8,9]] # 2차원, 2종 for문
aaa = [[[1,2],[3,4,5]],[[6],[7,8,9]]]
a = [1,2,3,4,5]
for i in a:
    print(i)
print("-"*50)    
for i in aa:
    for j in i:
        if isinstance(j,list):
            for k in j:
                print(j)
        else:
            print(k)