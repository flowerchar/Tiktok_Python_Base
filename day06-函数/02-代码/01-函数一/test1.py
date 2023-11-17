def add_num(num):
    return sum([i for i in range(1, num+1)])


print(add_num(100))

def add_num1(num):
    total = 0
    for i in range(1, num+1):
        total += i
        print(f'第{i}次的i的值是{i}, 截止到目前的总和是{total}')

    print(total)


add_num1(100)