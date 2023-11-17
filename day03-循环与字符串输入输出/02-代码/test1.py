import random

i=1
while i<=3:
    num = random.randint(1,9)
    if num==6:
        print("喜欢小狗")
        break
    i+=1
    # print(num)
else:
    print("喜欢小猫")