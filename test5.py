#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 创建数据库表
import MySQLdb
db = MySQLdb.connect("localhost","root","123","runoob")
cursor = db.cursor()
cursor.execute("drop table if exists runoob_tbl")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()