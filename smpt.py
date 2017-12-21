#!/usr/bin/python
# -*- coding: UTF-8 -*-
# SMTP发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 第三方SMT服务
mail_host = "smtp.qq.com"
# 用户名
mail_user = "1063658094@qq.com"
# 口令:qq邮箱设置->账号 SMTP设置 开启pop3/SMTP服务 获取口令 端口一般是465可以点击查到
mail_pass = "xxx"
# 发送者
sender = '1063658094@qq.com'
# 接收者 竟然可以自己给自己发，哈哈，如果不是qq邮箱的话，有些邮箱网易等会有反垃圾功能，收不到
receiver = ['1063658094@qq.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("George",'utf-8')
message['To'] = Header("未来战士", 'utf-8')
subject = '吃鸡游戏即将开始...小心地雷'
message['Subject'] = Header(subject, 'utf-8')
try:
	smtpObj = smtplib.SMTP_SSL(mail_host, 465)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receiver, message.as_string())
	smtpObj.quit()
	print "邮件发送成功"
except smtplib.SMTPException:
	print "Error: 无法发送邮件"
