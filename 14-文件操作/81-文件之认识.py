#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 3:31
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 81-文件之认识.py
#过程:打开->读、写->关闭
f=open('test.txt','w')
f.write('aaa')
f.close()
# 访问模式：r、w、a