A = ['张三', '李四', '王五']
B = ['看书', '睡觉', '打豆豆']
print([(value_a, value_b) for index_a, value_a in enumerate(A) for index_b, value_b in enumerate(B) if index_a==index_b])