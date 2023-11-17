num_list = input().split(',')
count = 0
for i in num_list:
    int_i = int(i)
    if int_i == 1:
        count += 1
        continue
    else:
        for j in range(2, int_i):
            if int_i%j == 0:
                break
        else:
            count += 1
print(count)