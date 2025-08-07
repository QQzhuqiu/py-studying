#列表
#基本格式：
#列表名 = [元素1,元素2，元素3..]
#注意：所有元素放在[]内，所有元素间用,隔开；元素间的数据类型，可以各不相同
#实例：
li = [1,2,3,4,5]
print(li,type(li))
print(li[0:3]) #列表也可以切片操作
#列表也是可迭代对象（可以for循环，便利取值）
for i in li:
    print(i)

#列表的相关操作
#一、添加元素
#append() 、 extend() 、 insert()
li = ['1','2','3','4','5']
li.append('6')
print(li)
#append() 整体添加
qu = ['one','two','three','four','five']
qu.extend('six')
print(qu)
#extend() 分散添加，将另一个类型中的元素逐一添加
#要用可迭代对象！整型不算可迭代对象；
co = ['one','two','three',]
co.insert(3,'six') # 在指定位置插入元素
co.insert(0,'seven') #指定位置有元素，原有元素后移
#co.insert('eight') #未指定位置就会报错：TypeError: insert expected 2 arguments, got 1
print(co)
#insert() 指定位置添加

#二、修改元素
#直接通过下标就可以进行修改
di = [1,2,3]
di[2] = 'a'
print(di)

#三、查找元素
#in：判断指定元素是否存在列表中，如果存在就返回True，不存在就返回False
#not in：判断指定元素是否存在列表中，如果不存在就返回True，存在就返回False
so = ['one','two','three']
print('one' in so)
print('twe' in so)
print('tow' not in so)
#实例：用户输入昵称，重复则不能使用
#定义一个列表，保存已经存在的昵称
'''
while True:
    name_list = ['coke', '5g', 'yuji']
    name = input('请输入昵称：')
    if name in name_list:
        print(f'用户名{name}已存在')
    else:
        print(f'用户{name}注册成功')
        # 把新昵称放入列表
        name_list.append(name)
        print(name_list)
        break
'''
# index：返回指定数据所在位置的下标，如果查找的数据不存在就会报错
# count：统计指定数据在所在列表中出现的次数
#和字符串用法相同

#四、删除元素
#del：删除元素
li = ['one','two','three']
del li[1] #根据下标删除
#del li 删除全表格
print(li)
#pop：删除指定下标的数据，python3版本默认删除最后一个数据
li = ['one','two','three']
li.pop() #默认最后一个元素
print(li)
co = ['one','two','three']
co.pop(1) #不能指定元素删除，只能根据下标删除
print(co)
#下标不能超出范围，否则报错：IndexError: pop index out of range
#remove：根据元素的值进行删除
li = ['one','two','three','two']
li.remove('two') #删除指定元素；且默认删除相同元素内第一个；
#li.remove('e') #列表中不存在的元素，删除了就会报错：ValueError: list.remove(x): x not in list
print(li)

#五、排序
#sort：将列表按特定顺序重新排列，默认从小到大
ke = [1,2,8,5,65,45]
ke.sort() #按照从小到大顺序排序
print(ke)
#reverse：倒叙，将列表倒置
co = ['one','two','three']
co.reverse()
print(co)

#六、列表推导式
#格式一：[表达式 for 变量 in 列表]
#注意：in后面不仅可以放列表，还可以放range()、可迭代对象
li = ['one','two','three']
[print(i) for i in li] # 前面的i是表达式
'''
定义一个空列表，用for循环添加元素并且集合在同一个列表
方法一：
co = []
for i in range(1,6):
    print(i)
    co.append(i)
print(co)
方法二：
nm = []
[nm.append(i) for i in range(1,6)]
print(nm)
'''
#格式二：[表达式 for 变量 in 列表 if 条件]
'''
实例：把奇数放在列表里面
方法一：
li = []
for i in range(1,6):
    if i % 2 == 1:
        li.append(i)
print(li)
方法二：
li = []
[li.append(i) for i in range(1,6) if i % 2 == 1]
print(li)
'''

#七、列表嵌套
#含义：一个列表里面又有一个列表
li = [1,2,3,[4,5]] #[4,5]是里面的列表
print(li[3]) #取出里面的列表
print(li[3][0]) #取出里面的列表中下标为0的元素


#元组
#基本格式：元组名 = (1,2,3)
#注意：所以元素包含在小括号内，元素与元素之间用,隔开，不同元素也可以是不同的数据类型
tua = (1,2,3,4)
print(type(tua))
tue = ('one',1,4,[1,2])
print(tue)
tub = (1,) # 只有一个元素的时候，末尾要加上,，否则返回唯一的值的数据类型
print(type(tub))

#元组与列表的区别
#不同点：
#1.元组只有一个元素时末尾必须加,，列表不需要
#2.元组只支持查询操作，不支持增删改操作
#相同点：
#1.元组和列表都有下标，也是从0开始
#2.元组和列表可用的查询操作相同count()、index()、len()
print(tua.index(2))
print(tua.count(4))
print(len(tua))
print(tua[1:]) #元组也可切片

#应用场景
# 函数的参数和返回值
# 格式化输出后面的()本质上就是一个元组
name = 'coke'
age = 18
print('%s的年龄是：%d' % (name,age))
info = (name,age)
print(type(info))
print('%s的年龄是：%d' % info)
#数据不可以被修改，保护数据的安全时可以用元组


#字典
#基本格式：字典名 = {键1:值1,键2:值2...}
#注意：键值对形式保存，键和值之间用:隔开，每个键值对之间用,隔开
dic = {'name':'coke','age':18}
print(type(dic))
print(dic)
#字典中的键具备唯一性，但是值可以重复
dic2 = {'name':'coke','name':18} # 键名重复不会报错，但前面的值会被后面的值覆盖
print(dic2)

#字典的常见操作
#一、查看元素
#变量名[键名]
dic = {'name':'coke','age':18}
#print(dic[2]) #字典中没有下标，所以不可以根据下标查询，否则报错：KeyError: 2，要通过键名去查询
print(dic['age'])
#print(dic2.('sex'))#键名不存在，查询后会报错：SyntaxError: invalid syntax
#变量名.get(键名)
dic = {'name':'coke','age':18}
print(dic.get('age'))
print(dic.get('tel'))
print(dic.get('tel','不存在')) #如果没有所查询的键名，则返回自己设置的默认值

#二、修改元素
#变量名[键名] = 值
#字典通过键名修改，列表通过下标修改
dic = {'name':'coke','age':18}
dic['age'] = 20
print(dic)

#三、添加元素
#变量名[键名] = 值
#注意：键名存在就修改，不存在就新增
dic = {'name':'coke','age':18}
dic['tel'] = 20 #此时没有tel健，新增进字典
print(dic)
dic['tel'] = 18 #此时已经有了tel，修改tel对应的值
print(dic)

#四、删除元素
#del
#1.删除整个字典：del 字典名
'''
dic = {'name':'coke','age':18}
del dic
print(dic) #报错，因为字典已经不存在：NameError: name 'dic' is not defined
'''
#2.删除指定健值对，键名不存在就会报错：del 字典名[键名]
dic = {'name':'coke','age':18}
del dic['age']
print(dic)
#clear()：清空整个字典内的东西，但保留了字典
dic = {'name':'coke','age':18}
dic.clear()
print(dic) #返回空字典
#pop()：删除指定键值对，键名不存在就会报错
dic = {'name':'coke','age':18}
dic.pop('age')
#dic.pop() #报错，没有指定键名
dic.popitem() #py3.7随机删除一个键值对，3.7之后默认删除最后一个键值对
print(dic)

#四、len()求长度
dic = {'name':'coke','age':18}
print(len(dic)) #因为字典中有2个键值对，所以返回2
li = ['one','two','three']
print(len(li)) #列表也可以求长度
st = 'apple'
print(len(st)) #字符串也可以求长度

#五、keys()：返回字典里面包含的所有键名
dic = {'name':'coke','age':18}
print(dic.keys()) #dict_keys(['name','age'])
#for循环取出键名
for i in dic: #只取出键名
    print(i)

#六、values()：返回字典里面包含的所有值
dic = {'name':'coke','age':18}
print(dic.values())
#for循环取出键值
for i in dic.values():
    print(i)

#七、item()：返回字典里面包含的所以键值对，健值以元组形式
dic = {'name':'coke','age':18}
print(dic.items())
#for循环取出键值对
for i in dic.items():
    print(i)
    print(type(i)) #元组形式

#字典的运用场景
#使用键值对，存储描述一个物体的相关信息


#集合
#基本格式：集合名 = {元素1,元素2,元素3...}
sl = {'one','two','three'}
print(sl,type(sl))
sl = {} #定义空字典
sk = set() #定义空集合
print(type(sl),type(sk))

#集合具有无序性
sl = {'one','two','three','four','five'}
print(sl) #每次运行结果都不一样
#集合无序的实现方式涉及hash表（了解）
print(hash('one'))
print(hash('two'))
#每次运行结果都不同，hash值不同，那么在hash表中的位置也不同，这就实现了集合的无序性
print(hash(1))
print(hash(2))
print(hash(3))
#python中int整型的hash值就是它本身，在hash表中的位置不会发生改变，所以顺序也不会改变
print(hash('1'))
print(hash('2'))
print(hash('3'))
#用引号括起来整型就变成了字符串，所以hash值还是会改变
#无序性：不能修改集合中的值

#集合具有唯一性，可以自动去重
sk = {'one','two','three','four','five'}
print(sk)

#集合的常见操作
#一、添加元素
#add 添加的是一个整体
s2 = {'one','two','three','four','five'}
print('原集合：',s2)
#集合的唯一性，决定了如果需要添加的元素与原集合中重复，就不进行任何操作
s2.add(1) #一次只能添加一个元素
print(s2)
s2.add((5,6))
print(s2)
#update 把传入的元素拆分，一个个放进集合中
s3 = {'one','two','three','four','five'}
print('原集合：',s3)
s3.update((5,6,8)) #元素必须是可迭代对象：字符串、列表、元组
print(s3)

#二、删除元素
#remove：选择删除的元素，如果集合中有就删除，没有就会报错
sr = {'one','two','three','four','five'}
sr.remove('five')
#sr.remove(3) #集合中没有3这个元素，则报错：KeyError: 3
print(sr)
#pop()：对集合进行无序排列，然后将左边的第一个元素删除
sr = {'one','two','three','four','five'}
print('原集合：',sr)
sr.pop() #默认删除根据hash表排序后的第一个元素
print('删除后：',sr)
#discard：选择要删除的元素，没有则不会发生任何改变和操作
sd = {'one','two','three','four','five'}
print('原集合：',sd)
sd.discard('five')
sd.discard(3) #无报错
print('删除后：',sd)

#交集和并集
#交集&
#含义：共有的部分
a = {'one','two','three','four','five'}
b = {'one'}
#b = {'six'} #如果没有共有部分，则返回set()空集合
print(a & b)
#并集 |
#含义：所以的都放一起，重复的不算（集合的唯一性）
a = {1,2,3,4}
b = {4,5,6,7}
print(a | b)
l = a | b
print(type(l))