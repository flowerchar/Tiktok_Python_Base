# 计数器控制 让偶数累加
"""
1. 准备累加的数据
2. 准备存储结果的变量
3. 循环计算
4. 输出结果
"""

i = 2
counter=0
result = 0
while i <= 100:
    result += i
    i += 2
    counter+=1
print(result)
print(counter)


