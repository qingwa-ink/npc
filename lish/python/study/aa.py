#!/usr/bin/python3
import keyword
 
# 英文测试
print("Hello, World!")

print("星期五") # 中文测试

'''
多行注释
输出关键字
需要 import keyword
'''
print(keyword.kwlist)

a = 99 / 4

if (a == 25):
  print ("a is 25")
else:
  print ("a is not 25")
  print (a)

# 单行过长可以用\换行
total = 99 + \
        100 + \
        200
print (total)

# 在 [], {}, 或 () 中的多行语句，不需要用\换行
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print (total)

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print (paragraph)

str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

