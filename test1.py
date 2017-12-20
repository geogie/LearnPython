#!/usr/bin/python
# -*- coding: UTF-8 -*-

#变量赋值
counter = 100
miles = 100.0
name = "John"
print counter,miles,name

# 字符串
str = 'Hello World'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "TEST"

# 列表
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist

# 元组
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple+ tinytuple

# 字典
dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = {'name': 'john', 'code':6734, 'dept':'sales'}
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()







