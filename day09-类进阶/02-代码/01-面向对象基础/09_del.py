import time

class Washer():
    def __init__(self):
        self.width = 300

    def __del__(self):
        print('对象已经删除')


haier = Washer()
haier_copy = haier
del haier

time.sleep(2)




