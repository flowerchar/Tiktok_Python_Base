number = eval(input())
for i in range(100, number+1):
    n1 = int(str(i)[0])
    n2 = int(str(i)[1])
    n3 = int(str(i)[2])
    if i == n1**3 + n2**3 + n3**3:
        print(i, end=' ')

