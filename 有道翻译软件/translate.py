# -*- coding:utf-8 -*-

import os
import urllib
#import urllib.request
#import urllib.parse
import json
a = 5
while a > 0:
    txt = input('输入要翻译的内容!')
    if txt == '0':
        break
    else:
                #os.chdir('e:\\python')
                url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'

                data = {
                # 自动翻译
                'from':'AUTO',
                'to':'AUTO',
                'smartresult':'dict',
                'client':'fanyideskweb',
                # 当前时间戳
                'salt':'1500092479607',
                'sign':'c98235a85b213d482b8e65f6b1065e26',
                'doctype':'json',
                'version':'2.1',
                'keyfrom':'fanyi.web',
                # 通过点击提交
                'action':'FY_BY_CL1CKBUTTON',
                'typoResult':'true'}

                data['i'] = txt

                data = urllib.urlencode(data).encode('utf - 8')
                wy = urllib.urlopen(url,data)
                html = wy.read().decode('utf - 8')
                print(html)

                ta = json.loads(html)
                print "翻译的内容是："+ta['translateResult'][0][0]['tgt'].encode('utf-8')
                a = a - 1