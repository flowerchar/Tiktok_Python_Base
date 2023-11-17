# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 数据1 ： 1 和 2  range(1,3)
# 数据2 ：0 1 2  range(3)
list1 = []
for i in range(1, 3):
    for j in range(3):
        # 列表里面追加元组： 循环前准备一个空列表，然后这里追加元组数据到列表
        list1.append((i, j))

# 1. i==1, j==0, (1,0)
# 2. i==1, j==1, (1,1)
# 3. i==1, j==2, (1,2)
# 4. i==2, j==0, (2,0)
# 5. i==2, j==1, (2,1)
# 6. i==2, j==2, (2,2)

print(list1)

# # 多个for实现列表推导式
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)


# 多for的列表推导式等同于for循环嵌套
