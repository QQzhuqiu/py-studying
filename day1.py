#1.python是什么
# python是面向对象的高级解释型计算机程序计算语言
#python是强类型的动态脚本语言
#2.第一个程序
# print("Hello SixStar")
#运行py文件

#3.bug
#print(“123”)
#输入错误(py中要用英文)
# print("123")
#缩进错误(要顶格)
#print("123") print("456")  
#语法错误
#print(123)
#命名错误，字符串要加""

#Debug中代码为蓝色时，表示是即将要运行的代表
# Show Excution Point显示当前代码的执行位置
# Step Into 下一步
# Run to Cursor运行到下一个断点的位置
# 总结：可以通过Debug来调试代码，查看错误信息

#4.注释
#单行注释  # print("123")  #这是单行注释
#注释内容不会被执行
#多行注释  
"""
print("123")
print("456")
print("789")
"""
#或者
'''print("123")
print("456")
print("789")
'''
#此外
#ctrl+/可以注释或取消注释选中的代码(使用的是单行注释)
#注释是用来解释代码的，帮助其他人理解代码的意图
#快捷键
#ctrl+z撤销
#ctrl+y重做
#ctrl+c复制
#ctrl+v粘贴
#ctrl+x剪切
#ctrl+a全选
#ctrl+f查找
#ctrl+h替换
#ctrl+s保存
#ctrl+shift+s另存为
#ctrl+shift+f格式化代码
#ctrl+shift+z重做
#ctrl+shift+c复制路径
#ctrl+shift+v粘贴路径
#ctrl+shift+u转换大小写
#ctrl+shift+e打开资源管理器
#ctrl+shift+p打开命令面板
#ctrl+shift+n新建窗口
#ctrl+shift+t重新打开关闭的标签页
#ctrl+shift+w关闭窗口
#ctrl+shift+q退出程序
#ctrl+shift+f12清除终端输出
#ctrl+shift+f11切换全屏模式
#ctrl+shift+f10运行当前文件
#ctrl+shift+f9切换断点
#ctrl+shift+f8切换调试模式
#ctrl+shift+f7查找下一个
#ctrl+shift+f6查找上一个
#ctrl+shift+f5停止调试
#ctrl+shift+f4关闭当前标签页

#5.输出print()
#values值
print("HHH","WWW","SSS") 
#输出多个值，默认用空格分隔(,号分隔)
#separator分隔符(sep)
print("HHH","WWW","SSS",sep=",")  
#SEP参数可以指定输出多个值时的分隔符
#end用来设定以...结尾，默认值是换行符\n，可以切换成其他字符串
print("HHH","WWW","SSS",sep=",",end="...")
#end参数可以指定输出结束时的字符串
#print(字符串，end="后面拼接的值"，最后结果为第一个print的字符串+end的值+第二个print的字符串)
#例如可以指定输出结束时的字符串为"..."，这样输出的结果就会是"HHH,WWW,SSS..."


#6.变量
#变量是用来存储数据的容器
#变量名由字母、数字、下划线组成，不能以数字开头，不能是关键字
#变量名区分大小写   
#变量名不能包含空格
#变量名不能使用特殊字符
#变量名不能是保留字
#变量名可以是任何有意义的名称
#变量名的命名规则
# 1.变量名只能包含字母、数字和下划线
# 2.变量名不能以数字开头
# 3.变量名不能包含空格
# 4.变量名不能使用特殊字符
# 5.变量名不能是保留字
# 6.变量名可以是任何有意义的名称
# 7.变量名区分大小写
# 8.变量名不能是关键字
# 9.变量名不能是内置函数名
# 10.变量名不能是内置模块名
# 11.变量名不能是内置类名
# 12.变量名不能是内置异常名
# 13.变量名不能是内置常量名
# 14.变量名不能是内置属性名
# 15.变量名不能是内置方法名 
# 16.变量名不能是内置函数名
# 17.变量名不能是内置模块名
