# 需求：尝试以r打开文件，如果有异常以w打开这个文件，最终关闭文件
try:
    f = open('test100.txt', 'r')
except Exception as e:
    f = open('test100.txt', 'w')
finally:
    print("不管有无异常都会执行这句话")
    f.close()



