#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 3:58
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 84-文件之readlines.py
#readlines 按行的方式把整个文件内容读取，返回结果是列表，每一行为一个元素
f=open('test.txt','r')
print(f.readlines())# 列表
f.close()
#readline 按行的方式把整个文件内容读取,只读取一行
f=open('test.txt','r')
print(f.readline())# 一个
print(len(f.readline())) #存在\n
f.close()