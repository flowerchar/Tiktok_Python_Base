sentence = input('请输入字符串：')
while True:
    if len(sentence)>31:
        sentence = input('请输入字符串：')
    else:
        break
set1 = set(sentence)
dict1 = {letter:sentence.count(letter) for letter in set1}
print(f'您输入字符串：{sentence}\n长度：{len(sentence)}\n逆序后为：{sentence[::-1]}')
print(f'字符统计结果为：{dict1}')
