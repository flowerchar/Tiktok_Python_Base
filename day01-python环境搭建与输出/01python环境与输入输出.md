# **01Python环境与输入输出**

## 一、Python介绍

### 1.1 计算机组成

- 常见的计算机：![image-20231030102124148](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030102124148.png)
- 计算机组成分为：计算机**硬件组成**以及计算机**软件组成**
- 硬件组成：
  - 运行原理图![image-20231030102334414](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030102334414.png)
  - 现实里的硬件![image-20231030102553879](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030102553879.png)
- 软件组成分为**系统软件**和**应用软件**
- 系统软件是连接底层硬件和应用软件的“中间件”，我们使用的日常软件都是基于系统软件。比如计算机操作系统：Windows、Mac、Linux。手机操作系统：Android、IOS、Symbian等等
- 应用软件是某一类特定用途的软件。比如影音类、通讯交流类、办公编辑类

### 1.2 Python简介

- Python是一个荷兰人在1989年圣诞节无聊时开发的一个编程语言
- Python的优点：
  - 学习成本低
  - 使用领域广泛
  - 第三方生态强大
- 各个语言创始人![image-20231030104217369](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030104217369.png)

### 1.3 课程介绍

- 学习路线：
  - Python入门
    - 环境搭建
    - 变量
    - 输入输出
    - 数据类型
  - 流程控制
    - 条件语句
    - 循环
  - 数据序列
    - 字符串
    - 列表
    - 字典
    - 元组
  - 函数
    - 参数
    - 返回值
    - 递归
    - lambda表达式
  - 面向对象
    - 类和对象
    - 继承
    - 面向对象高级
  - 模块、包、异常
- 编译型与解释型
- 计算机只能识别二进制码(0101100)。我们需要把人类能看懂的代码变成机器可以执行的01代码
- 编译是一次性把代码编译成二级制代码交给计算机执行
- 解释是读取一段代码解释执行一段，直到结束
- 编译可以理解为把一份英语文档交给翻译软件，软件一次就直接翻译成汉字；解释相当于即时翻译，出差去国外交流，需要两边都有翻译家即时翻译每一段语句。![image-20231030112040729](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030112040729.png)

## 二、注释

<span style="color:blue;">myFirstPython</span>

- 注释是为了让使用者了解某段内容，比如古诗文注释、作者生活背景注释、器具使用注释![image-20231030112527132](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030112527132.png)
- 有时候并不能一眼看出来一段代码的作用，那么就可以书写注释，既能让自己了解透彻，又能方便其他开发者快速上手。这就是用注释增加代码的可读性
- 注释分为两类：**单行注释**和**多行注释**
- 单行注释是在注释信息内容前面添加**#**
- 多行注释是在注释信息内容前后添加”””

<span style="color:blue;">01-注释</span>

## 三、变量

- 程序中的数据都是存放在内存中的，需要通过某个变量"引用"指向数据![image-20231030113143419](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030113143419.png)![image-20231030113204289](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030113204289-1698636727485-1.png)![image-20231030113224498](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030113224498.png)![image-20231030113236422](01python%E7%8E%AF%E5%A2%83%E4%B8%8E%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.assets/image-20231030113236422.png)

- 我们不能直接访问内存里面的数据，但是可以让变量指向这块区域，然后操作该变量

- 变量命名要见名知意

- Python变量命名规则：

  - 由数字、字母、下划线组成
  - 不能数字开头
  - 不能使用内置关键字
  - 严格区分大小写

- 好的变量名：

  - currentAge(小驼峰，通常作用于属性和方法)
  - firstName
  - FlappyBird(大驼峰，通常作用于类)

- 非法的变量名：

  - 100age
  - hello World
  - (abc

- | 数值型数据类型 | 描述   |
  | -------------- | ------ |
  | int            | 整型   |
  | float          | 浮点型 |
  | bool           | 布尔型 |

- | 非数值型数据类型 | 描述   |
  | ---------------- | ------ |
  | str              | 字符串 |
  | list             | 列表   |
  | tuple            | 元组   |
  | set              | 集合   |
  | dict             | 字典   |

- Python是动态语言，变量的类型以最后一次操作为准

<span style="color:blue;">02-变量</span>

<span style="color:blue;">03-认识bug</span>

<span style="color:blue;">04-认识数据类型</span>

## 四、补充

### 4.1 f-格式化

- f-格式化字符串是python3.6中新增的方法，支持3.6以及以上的版本，效率比传统的格式化方式高

- f-格式化适用于一段静态+动态的字符串。比如打印这样一段文字："学号{id}的同学，性别为{sex}，身高{height}"。对于非大括号部分都是不变的，变动的只有id、sex、height

<span style="color:blue;">05-f格式化字符串</span>

### 4.2 转义字符

- 用特定字符表达特殊含义，此时转义字符就不是原本的字符意思了
- \n：是换行符，跟回车键功能一样
- \t :  是制表符，代表四个英文字符大小的位置 
- print函数中end参数默认值是\n，会自动换行

<span style="color:blue;">06-转义字符</span>

<span style="color:blue;">07-print结束符</span>

## **作业**

1. 将自己的姓名，性别，年龄，手机号等个人信息使用变量的形式在程序中保存；将定义的个人信息打印显示出来

2. 用户输入用户名和密码， 并控制台格式化输出用户输入的用户名和密码。

3. 书写程序，制作一个加法计算器。

   用户依次输入2个整数，系统自动进行加法运算，并打印结果

4. 开发程序：购物车功能。

   已知A网站苹果和橘子两种水果单价(具体如下)，用户根据自己的需求输入斤数， 系统计算总价并打印结果。

   ```python
   # 水果单价
   apple_price = 6.6
   orange_price = 5
   ```



答案：

```python
name = "TOM"
age = 18
weight = 66.6

print(f'姓名: {name}, 年龄: {age}, 体重: {weight}公斤')
```

```python
user_name = input('请输入用户名：')
user_pwd = input('请输入密码：')

print(f'您输入的用户名是{user_name}, 密码是{user_pwd}')
```

```python
num1 = input('请输入数字1：')
num2 = input('请输入数字2：')

result = int(num1) + int(num2)

print(result)
```

```python
# 水果单价
apple_price = 6.6
orange_price = 5

# 用户输入购买斤数
apple_weight = float(input('请输入要购买苹果的斤数：'))
orange_weight = float(input('请输入要购买橘子的斤数：'))

# 计算总价
result = apple_price * apple_weight + orange_price * orange_weight

print(f"这次购物共需要支付{result}元" )
```



****
