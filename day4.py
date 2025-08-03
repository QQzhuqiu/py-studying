#if判断
#基本格式
#if 判断条件：
#   满足条件做的事情
#实例一：
age = 17
if age < 18:
    print('未成年不能上网')
else:
    print('欢迎光临')
#实例二：
'''
score = input('请输入成绩：')
if score == '100':
    print("你真棒！")
if score == '60':
    print("还要继续加油哈！")
'''

#运算符
#一、比较（关系）运算符
# == 比较的是两个变量的值是否相等，相等就返回为True，否则为False
# != 比较的是两个变量的值是否相等，不相等就返回为True，否则为False
a = 666
b = 999
print(a != b)
if a < b:
    print('a小于b')
#二、逻辑运算符
# and 左右两边都符合才为True
a = '嘿嘿'
b = '哈哈'
if a == '嘿嘿' and b == '哈哈':
    print('你笑密码呢')
# or 左右两边一边符合就为True
fruit = '苹果'#室友带的水果
if fruit == '苹果' or fruit == '香蕉':
    print('带回来了水果')
# not 相反的结果
print(not 3>9)
#三、三目运算(三元表达式)
#格式：为真结果 if 判断条件 else 为假结果
a = 8
b = 5
if a < b:
    print('a小于等于b') #为真结果
else:
    print('a比b大') #为假结果
print('a小于等于b') if a <= b else print('a比b大')

#if-else
#基本格式
#if 条件:
#   满足条件时要做的事
#else:
#   不满足条件时要做的事
a = 666
if a == 999:
    print("你真棒！")
else:
    print("还要继续加油！")

#if-elif
#区别：if-else二选一；if-elif多选一
'''
if 条件1:
    满足条件1要做的事情
elif 条件2:
    满足条件2要做的事情
elif 条件3:
    满足条件3要做的事情
'''
#前面条件满足，就不会判断后续条件
#实例：
score = 100
if 85 <= score <= 100:
    print('优秀')
elif 60 <= score <= 85:
    print('及格')
elif 0 <= score < 60:
    print('不及格')
else: #加上else，构成if-elif-else结构
    print('分数无效')
#else可以表示所有条件都不符合的情况

#if嵌套
#格式：
'''
if 条件1:
    事件1
    if 条件2:
        事情2
else:
    不满足条件做的事情
'''
#注意：内外层if判断都可以是if-else结构（或者if-elif/if-elif-else结构）
#实例：
#定义一个布尔型变量，表示是否有车票
#定义一个浮点型变量保存体温
ticket = True #True表示有车票，False表示没车票
temp = 38.5
picture = 'green'
if ticket == True: #判断是否有车票
    print('欢迎乘坐列车')
    #正常人腋下体温是36.3-37.2
    if 36.3 <= temp <= 37.2:
        print('体温正常，可以通行')
    elif picture == 'green':
        print("健康码为绿吗，可以通行")
    else:
        print('体温异常，请配合检查，谢谢！')
else:
    print('抱歉，没有车票不能进站')

#循环语句
#一、while循环
#基本语法：
'''
定义初始变量
while 条件:
    循环体(条件满足时段做的事情)
    改变变量
'''
i = 1 # 定义一个初始值，记录循环次数，i = 1 表示从第一次开始
while i <= 2:
    print('好好学习，天天向上！')
    i += 1 # 每执行一次，i的值+1
# 注意：如果没有改变变量，条件一直满足，就是一直循环下去，一直执行；
#死循环：
'''
while True:
    循环体
'''
#while True/1/2/...: #条件只写True，说明一直为真，就会一直执行，从而形成一个死循环；False则不输出
#   print("永远18岁")
#while循环的运用：计算1加到100的总和
i = 1 #定义一个初始值，从1开始计算，记录循环次数
s = 0 #定义一个变量，保存计算结果，最开始计算结果为0
while i <= 100:
    print(i)  #循环打印1-100
    s += i    #每次循环结果结果和i进行相加
    i += 1    #每循环一次，i值+1
    #print('计算结果是：',s) #在循环内，循环输出计算结果
print('计算结果是：',s) ##在循环外，循环输出最终计算结果

#二、while循环嵌套
#含义：一个while循环里面还有一个while循环
#基本格式：
'''
while 条件1:
    循环体1
    while 条件2:
        循环体2
        改变变量2
    改变变量1
'''
#注意：缩进决定层级，严格控制缩进，最好自动缩进
i = 1 # 定义一个变量记录外循环的次数
while i <= 3: #外循环
    print(f"这是第{i}此外循环")
    j = 1 #定义一个初始值记录内循环的次数
    while j <= 5: #内循环
        print(f"内循环{j}次")
        j += 1
    i += 1

#for循环
#基本格式：
'''
for 临时变量 in 可迭代对象:
    循环体
'''
#注意：冒号和缩进！
str = '123' #定义一个字符串
#可迭代对象就是要去遍历取值的整体（如str），现在的话只要记住字符串就是可迭代对象
for i in str: # i是临时变量，可随便写
    print(i)
#如果想计数，可以用range函数

#range函数
#用来记录循环次数，相当于一个计数器
#range(start,stop,step)
#start，stop，step三个参数可都写，也可只写其中一个
for i in range(1, 10): # 从1开始，从10-1结束，遵循包前不包后规则，类似于数学中[)，左闭右开
    print(i)
#包前不包后：包含开始位置的数字，不包含结束位置的数字
#range()里面只写一个数，这个数就是循环的次数，默认从0开始
#写两个数，前面数字表示开始位置，后面数字表示结束位置

#for循环应用：计算1+2+...+100的值
s = 0 #定义一个变量，保存计算结果，最开始计算结果为0
for i in range(1, 101):
    #print(i)
    s += i
    #print('最终计算结果为：', s) #在循环内，循环输出计算结果
print('最终计算结果为：',s) #在循环外，循环输出计算结果
#相比之下，for循环更简便一些，更常见

#break和continue关键字
#共同点：都是在循环中使用的关键字
# i = 1
# if i <= 5:
#     print('我在吃苹果')
#     break
#报错：break和continue只能放在循环内
#一、break
#作用:某一条件满足时，退出循环
i = 1
while i <= 5:
    print(f'coke吃第{i}个苹果')
    if i==3:
        print("吃饱啦")
        break
    i += 1

#二、continue
#作用：退出本次循环，下一次循环继续执行
i = 1
while i <= 5:
    print(f'coke在吃第{i}个苹果')
    if i==3:
        print(f'吃到史了，第{i}个苹果不吃了')
        #在continue之前，一定要修改计数器，否则会陷入死循环
        i += 1 #关键！
        continue
    i += 1

for i in range(5):
    if i == 3:
        #break   # i=3时结束当前所在循环
        continue #跳过3，结束了在3时的循环，继续执行下一个循环
    print(i)
