typle1 = ("tom","kaisa","alisi","xiaoming","songshu")
#1. 用元组取下标为2的值
print(typle1[2])
#2. 可以利用切片从下标2开始取到下标3之前
print(typle1[2:3])
#3. 可以用for循环来遍历所有的值，判断，如果有一个是alisi，那就输出
for i in typle1:
  if i == "alisi":
    print(i)