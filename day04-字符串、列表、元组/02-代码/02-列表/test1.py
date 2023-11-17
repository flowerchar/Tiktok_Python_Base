users = ['root', 'admin']
passwd = ['123', '456']
username = input('请输入用户名：')
password = input("请输入密码：")
if username in users:
    if password in passwd:
        print("登陆成功")
    else:
        print("密码错误")
else:
    print("用户名不存在")