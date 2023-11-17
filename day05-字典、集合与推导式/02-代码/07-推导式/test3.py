int_list = [i for i in range(1, 101)]
print([[i-2, i-1, i] for i in int_list if i%3==0])