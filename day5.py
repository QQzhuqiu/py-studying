#一、字符串编码
#本质上就是二进制数据与语言文字的一一对应的关系
#1.Unicode：所有字符都是2个字节；
# 好处：字符与数字之间转换速度更快一些；
# 坏处：占用空间大；
#2.UTF-8：精准，对不同字符用不同的长度表示；
# 好处：节省空间；
# 坏处：字符与数字的转换速度慢，每次都需要计算字符需要多少个字节表示；

#二、字符串编码转换
a = 'hello'
print(a,type(a)) # str,字符串是以字符为单位进行处理
a1 = a.encode()  # 编码
print('编码后：',a1)
print(type(a1))  # bytes，以字节为单位进行处理
a2 = a1.decode()  # 解码
print(a2,type(a2))
# 注意：对于bytes，只需要知道它跟字符串之间的互相转换
st = "这里是六"
st1 = st.encode("utf-8")
print(st1,type(st1))
st2 = st1.decode()
print(st2,type(st2))

#三、字符串常见操作
#1. + 字符串拼接
print(10 + 10) #20,真型相加，+是算数运算
print('10' + '10') # 1010,字符串相加，+是字符串拼接
name1 = 'coke'
name2 = '老师'
print(name1 + name2)
print(name1 , name2 , sep = "")
#两种写法
#2.重复输出
print("好好学习，天天向上"*5)
print("好好学习，天天向上\n"*5) # 加入换行符
#需要输出多少次，在*后输入数字
#3.成员运算符
#作用：检测字符串中是否包含了某个子字符串（即某个字符或多个字符）
# in: 如果包含的话，返回True, 不包含返回False
# not in: 如果不包含的话，返回True，包含返回False
name = 'bingbing'
print('b' in name)  #True
print('a' in name) #False
print('b' not in name) #False
print('a' not in name) #True
print('bin' in name) #True
print('binb' in name) #False

name = '冰冰'
print('six' in name) #False
print('冰冰' in name) #True
print('冰水' not in name) #True