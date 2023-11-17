a_dict={'张三':60, '李四':98, '王五': 100, '赵六':50}
print({index: value for index, value in a_dict.items() if value >= 60})