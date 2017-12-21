#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 数据库插入操作
import MySQLdb
db = MySQLdb.connect("localhost","root","123","runoob")
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()