#!/usr/bin/python3

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
 
print (counter)
print (miles)

# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"
print (a, b, c)
print (isinstance(a, int))
print (isinstance(counter, float))
print (isinstance(miles, float))
print (type(counter), type(miles), type(c))

# 删除对象引用
del a, b
# print (a)  # 打印报错：NameError: name 'a' is not defined

# 乘方
c = 2 ** 5
print (c)

# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数
c = 9 / 2
print (c)
c = 9 // 2
print (c)

# list操作
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

# 列表中的元素是可以改变的
a = [1, 2, 3, 4, 5, 6]
print (a[1:4:2])   # 索引 1 到索引 4 的位置并设置为步长为 2
a[0] = 9
a[2:5] = [13, 14, 15]
print (a) 
a[2:5] = []
print (a) 

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
