#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 12:39
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 85-文件之seek函数.py
#r
f=open('test.txt','r+')
f.seek(2,0) # 0:开始 1:当前 2:结束 相对于访问模式中指针位置
print("-"*10+'r模式'+'-'*10)
print(f.read())
f.close()
#a
f=open('test.txt','a+')
f.seek(2,0) # 0:开始 1:当前 2:结束 相对于访问模式中指针位置
print("-"*10+'a模式'+'-'*10)
print(f.read())
f.close()