MAX = -1
MIN = 151
SUM = 0
counter = 0
while True:
    number = eval(input(f"请输入第{counter+1}个的成绩："))
    if number == -1:
        break
    if MAX < number:
        MAX = number
    if MIN > number:
        MIN = number
    SUM += number
    counter += 1

print(f'输入的数据中最大值是{MAX}\n最小值是{MIN}\n总和是{SUM}\n平均值是{SUM/counter}')