str1 = 'hello world'
counter = 0
for i in str1:
    if i == 'l':
        counter += 1
        if counter == 3:
            continue
    print(i)