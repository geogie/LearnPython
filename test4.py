#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
# host，user，password，数据库名字
db = MySQLdb.connect("localhost","root","123","RUNOOB")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
# 数据库版本号
print "Database version : %s " % data
db.close()
