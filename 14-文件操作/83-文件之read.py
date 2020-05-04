#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 3:51
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 83-文件之read.py
f=open('test.txt','r')
print(f.read(10))# 10为长度
f.close()