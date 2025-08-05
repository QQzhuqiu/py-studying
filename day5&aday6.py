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


#4、下标
#python中下标从0开始
#作用：通过下标能够快速找到对应的数据
#格式：字符串名[下标值]
name = 'coke'
#从左往右数，下标从0开始
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#print(name[4]) #报错，取值的时候不用超出下标范围
#从右往左数，下标从-1开始，-1，-2...
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
#print(name[-5]) #报错，超出下标范围


#5、切片
#含义：指对操作的对象截取其中一部分的操作
#语法：[开始位置:结束位置:步长]
#遵循包前不包后规则：即从起始位置开始，到结束位置的前一位结束（不包含结束位置本身）
st = 'cokelaodi'
print(st[0:4]) # coke
print(st[4:7]) # lao
print(st[4:])  # laodi    下标为4之后的全部截取到
print(st[:8])  # cokelaod 下标为8之前的全部截取到，不包含8
#从右往左
print(st[-1:]) #i
print(st[:-1]) #cokelaod
#print(st[-1:-5]) #步长默认为1，与切取方向不一致，无法取值
#步长：表示选取间隔。不写步长，则默认是1
#步长的绝对值大小决定切取的间隔，正负号决定切取方向。
#正数表示从左往右取值，负数表示从右往左取值
print(st[-1::-1])   #idoalekoc
print(st[-1:-5:-1]) #idoa
print(st[0:9:3])    #ceo
#print(st[0:7:3])中'3'为步长，即'c'ok'e'la'o'di
#切取方向要一致，否则切取不到值


#6.查找
#①find：检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就返回-1
#格式：find(子字符串,开始位置下标,结束位置下标)
#注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = 'coco'
print(name.find('c'))     # 0 第一个c的下标为0
print(name.find('co'))    # 0 检测到第一个co，c的下标为0
print(name.find('c',2))   # 2 从第2个位置开始寻找到第一个c的下标为2
print(name.find('c',5))   # -1 超出范围，不包含返回-1
print(name.find('c',0,2)) # 0 在下标0-2位置范围内查找
#包前不包后
print(name.find('c',3,4)) #-1 超出范围

#②index()：检测某个子字符串是否包含在字符串内，如果在就返回这个子字符串开始位置的下标，否则就会报错
#格式：index(子字符串,开始位置下标,结束位置下标)
#注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = "我勒个骚钢啊"
print(name.index('个'))     # 2
#print(name.index('个',3))  # 报错：ValueError: substring not found 从下标3开始找，没有找到
print(name.index('个',0,3)) # 2
#遵循包前不包后规则
#区别：find没找到，返回-1；index没找到就会报错

#③count()：返回某个子字符串在整个字符串中出现的次数，没有就返回0
#格式：count(子字符串,开始位置下标,结束位置下标)
#注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = 'apple'
print(name.count('p'))      #2
print(name.count('x'))      #0
print(name.count('e',0))    #1
print(name.count('p',0,5))  #2
#遵循包前不包后规则


#7，判断
#均遵循包前不包后规则
#①startswith()：是否以某个子字符串开头，是的话就返回True，不是的话就返回False，如果设置开始和结束位置下标则在指定范围内检查
#格式：startswith(子字符串,开始位置下标,结束位置下标)
st = 'purchase'
print(st.startswith('pur'))     #True
print(st.startswith('cha'))     #False
print(st.startswith('r',2,4))   #True

#②endswith()：是否以某个子字符串结尾，是的话就返回True，不是的话就返回False，如果设置开始和结束位置下标则在指定范围内检查
#格式：endswith(子字符串,开始位置下标,结束位置下标)
st = 'purchase'
print(st.endswith('pur'))     #False
print(st.endswith('se'))      #True
print(st.endswith('c',2,4))   #True

#③isupper()：检测字符串中所以的字母是否都为大写，是的话就返回True
st = 'purchase'
print(st.isupper()) #False
print('PUR'.isupper()) #True

#④islower()：检测字符串中所以的字母是否都为小写，是的话就返回True
st = 'purchase'
print(st.islower())     #True
print('PUR'.islower())  #False

#8.修改元素
#①replace()：替换
#格式：replace(旧内容,新内容,替换次数)
#注意：替换次数可以省略，默认全部替换
name = 'cyx爱爱吃'
print(name.replace('cyx','lch'))  #lch爱爱吃
print(name.replace('爱','喜欢',1)) #cyx喜欢爱吃

#②split()：指定分隔符来切字符串
#格式：split('分割内容'，分割次数)
st = 'purchase,apple'
print(st.split(','))   #['purchase', 'apple'],以列表的形式返回
#如果字符串中不包含分割内容，就不进行分割，会作为一个整体
print(st.split('o'))   #['purchase,apple']
print(st.split('a'))   #['purch', 'se,', 'pple']
print(st.split('a',1)) #['purch', 'se,apple'],指定只分割一次

#③capitalize()：第一个字符大写，其他都小写
st = 'purchase'
print(st.capitalize()) # Purchase

#④lower()：大写字母转为小写
st = 'PurChaSe'
print(st.lower())  #purchase

#⑤upper()：小写字母转为大写
st = 'purchase,apple'
print(st.upper()) #PURCHASE,APPLE