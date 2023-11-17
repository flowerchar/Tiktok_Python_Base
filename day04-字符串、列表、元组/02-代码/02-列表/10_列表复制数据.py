name_list = ['TOM', 'Lily', 'ROSE']

list1 = name_list.copy()
list2 = name_list # list2 name_list指向的是同一个引用
list3 = name_list[::]
name_list[0] = 'lol'
print(name_list)
print(list1)
print(list2)
print(list3)
print('------')
