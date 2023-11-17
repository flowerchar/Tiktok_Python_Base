# 需求：1-100数字累加和 -- 1 + 2 + 3 + 4...+ 100 = 结果，打印结果
"""
1. 准备做加法运算的数据 1- 100 增量为1
2. 准备变量保存将来运算的结果
3. 循环做加法运算
4. 打印结果
5. 验证结果正确性
"""

# 准备数据
i = 1

# 结果变量
result = 0

# 循环
while i <= 100:
    # 加法运算 前两个数的结果 + 第三个数 -- 每计算一次加法则更新一次result变量值

    print(f'第{i}次， i的值是{i}, result变化值前的值是{result}', end='-------->')
    result = result + i
    print(f'变化之后的result的值是{result}')
    i += 1
# 打印最终结果
print(result)

# 1.i==1, i<=100, True, result=0+1=1, i=2
# 2.i==2, i<=100, True, result=1+2=3, i=3
# 3.i==3, i<=100, True, result=3+3=6, i=4
# 4.i==4, i<=100, True, result=6+4=10, i=5
# 5.i==5, i<=100, True, result=10+5=15, i=6
# ...
# 99.i==99, i<=100, True, ..., i=100
# 100. i==100, i<=100, True, ..., i=101
# 101. i==101, False


# 1.i==1, i<=100, True, i=2, result=0+2=2
# 2.i==2, i<=100, True, i=3, result=2+3
# 3.i==3, i<=100, True, result=3+3=6, i=4
# 4.i==4, i<=100, True, result=6+4=10, i=5
# 5.i==5, i<=100, True, result=10+5=15, i=6
# ...
# 99.i==99, i<=100, True, ..., i=100
# 100. i==100, i<=100, True, ..., i=101
# 101. i==101, False
