#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "Hello, Python!";

# 格式严格缩紧
if True:
	print "Answer"
	print "True"
else:
    print "Answer"
    print "False"

# 等待用户输入
raw_input("\n\nPress the enter key to exit.")

# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x="a"
y="b"
# 换行输出
print x
print y

print '----------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y

# 使用sys模块，sys.argv命令行参数，sys.argv[0]文件本身路径
import sys
print sys.argv
print sys.argv[0]

