# 1. 函数：固定数据1 和 2 加法
def add_num1():
    result = 1 + 2
    return result


res = add_num1()
print(res)
# print(result)

# 2. 参数形式传入真实数据  做加法运算
def add_num2(a, b):
    result = a + b
    print(result)


add_num2(10, 20)

add_num2(100, 200)

# add_num2(100)  # 报错，定义函数有2个参数，传入数据也要是2个
#
# def operation_num(num1, num2, sign):
#     if sign=='+':
#         print(num1+num2)
#     elif sign=='-':
#         print(num1-num2)
#
# operation_num(1,3,'+')
# operation_num(1,3,'-')

