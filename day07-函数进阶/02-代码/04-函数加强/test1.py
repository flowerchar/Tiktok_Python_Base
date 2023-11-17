# 元素按照最后一个字母从大到小排序
l = ['abd','ewetrwef','ferea','qwszfgfsaffs']
l.sort(key=lambda x:x[-1], reverse=True)
print(l)
