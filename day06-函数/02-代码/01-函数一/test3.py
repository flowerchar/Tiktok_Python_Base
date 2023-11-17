import random

def A():
    return random.randint(0, 10)
def B():
    print(f'已经休眠了{A()}秒，开始工作了')

B()