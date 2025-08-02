#数值类型
#1.int整数型（任意大小的整数）
num1 = 1
#检测数据类型的方法 type()
print(type(num1))
#2.float浮点数（小数）
num2 = 1.5
print(type(num2))
#3.bool布尔型（重点）
#通常用于判断
#固定写法：一个为True，一个为False
print(type(True))
#True&False必须严格区分大小写
#布尔值可以当作整型对待，True相当于整数1，False相当于整数0
print(True + False)
#4.complex复数型
#固定写法： z = a + bj
#a是实部，b是虚部，j是虚数单位
print(type(2 + 3j))
#用于数据运算
#j是固定虚数单位，不能随意改变，否则语法错误

#字符串
#特点：需要加上引号（单/双），多行内容可以三引号
#name = sixstar
#报错，没有引号识别为变量名，sixstar未被赋值
name = 'sixstar'
name = "sixstar"
name = """sixstar
骚钢啊"""
#多行注释和字符串用三引号包含的区别是，多行注释是单独存在，不需要变量名赋值，而字符串需要；

#格式化输出
#占位符：生存一定格式的字符串
#一、%的用法：①%s 字符串（常用）
name = "coke"
print("我的名字是: %s"% name)
#占位符只占位，不输出
#②%d 整数（常用）
age = 18
name = "coke"
print("我的名字是：%s，年龄：%d"%(name,age))
#%4d 整数
#数字设置位数，不足前面补空白
a = 91
print("%6d"% a)
print("%06d"% a)
print("%02d"% a)
#不足用0补全
#④%f 浮点数（常用）
a = 1.2
print("%f"% a)
#默认后六位小数，遵守四舍五入原则
#⑤ %.4f 浮点数
#数字设置小数位数，遵循四舍五入原则
b = 9.111111111
print("%7f"% b)
#默认显示七位小数
#⑥ %%
print("我是%%的1%%"%())
#二、f格式化
#格式：f"{表达式}"
name = 'coke'
age = 18
print(f"我的名字是{name},年龄{age}了")

#算术运算符
#优先级：幂>乘、除、取余、取整>加减
print(1+1)
print(2-2)
print(3*3)
print(4/4)#商一定是浮点数
#且除数不能为0，否则报错：ZeroDivisionError: division by zero
#// 取整：不管四舍五入原则，只要后面有小数，就忽略小数
print(5//5)
a = 9
b = 3
c = 9.0
print(a // b)
print(c // b)#使用算术运算符，其中若有浮点数，结果必定用浮点数显示
#% 取余数：只取余数
print(a % b)
#** 幂 m**n：m的n次方
print(a ** b)
print(a ** b + c/2)

#赋值运算符
#一、给变量赋值
num1 = 8
num2 = 9
#将一个变量的值赋给另一个变量
num3 = num1
print(num3)
num4 = num2
print(num4)
#将运算的值赋给变量
total = num3 + num4
print(total)
#二、①+=
a = 1
print(a)
#a = a + 1
a += 1 #等效于a = a + 1
print(a)
#实例：
n1 = 99#成本
n2 = 66#利润
n1 += n2 #等效n3 = n1 + n2 #售价
print(n1)
print(n2)#n2无变化
#二、②-=
b = 1
print(b)
#b = b - 1
b -= 1#等效b = b - 1
print(b)
#赋值运算符中间不可以有空格，否则语法错误
#只能针对已经存在的变量
'''
反例：
n += 10 
n未被定义，所以不能参与加法运算
'''
#纯数字不能使用赋值运算符，否则语法错误，因为赋值运算符是针对变量存在的

#input()输入函数
#input(prompt) #prompt是提示，会在控制台中提示
'''
name = input("请输入姓名：")
print(name)
pwd = input("请输入你的密码：")
print(pwd)
'''

#转义字符
#\t 制表符:通常表示空四个字符，也称缩进
print('sixs\tar')
print("姓名\t年龄\t电话\t")
#\n 换行符：表示将当前位置移到下一行开头
print("压力\n暴大")
#\r 回车：表示将当前位置移到本行开头
print("sixsta\r哇哈哈哈哈哈哈")
#\\ 反斜杠符合
print('sixs\\tar')
print(r'sixsta\\tar')# r原身字符串，默认取消转义.

