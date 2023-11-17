a="abcdef"
a1='ace'
print(a[0:-1:2])
print(a[0:-1:2][::-1])
print(a1[::-1])
print('-------------------')
print(a[1:5:2])
print(a[::-2])
print(a[5:1:-2])

# username = input('please enter your username->: ')
# password = input('please enter your password->: ')
# if 6<=len(username)<=20:
#     if username[0].isalpha():
#         if len(password)>=6:
#             if not password.isnumeric():
#                 if password.find(' ') == -1:
#                     print('校验成功，登陆!')
#                 else:
#                     print('登录失败！密码中有空格')
#             else:
#                 print('登录失败！密码是纯数字')
#         else:
#             print('登录失败！密码长度小于6位')
#     else:
#         print('登录失败！用户名不是以字母开头')
# else:
#     print('登录失败！用户名长度不在6-20之间')