#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 汇率兑换
# 汇率
USD_VS_RMB = 6.77

# 人民币的输入
try:
    rmb_str_value = input('请输入人民币(CNY)金额(注意直接输入数字不要加特殊字符)：')
    print '输入的数据类型：',type(rmb_str_value)
    # 汇率计算
    usd_value = rmb_str_value / USD_VS_RMB
    # 输出结果
    print '美元(USD)金额是：', usd_value
except NameError:
    print "输入格式错误，请输入数字(可以带小数)"