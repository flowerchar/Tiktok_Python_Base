# 接收所有位置参数，返回一个元组
def user_info(*args1):
    print(args1)


user_info('TOM')
user_info('TOM', 20)
user_info('TOM', 20, 'man')
user_info()

