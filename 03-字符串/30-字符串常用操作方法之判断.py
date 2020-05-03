#-*- coding: utf-8 -*-
# @Time    : 2020/4/30 23:50
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 30-字符串常用操作方法之判断.py

mystr = "hello world and itxxxx and xxwwwds and Python"
#1.startswith('') 以什么字符开头
print(mystr.startswith('hell'))
#2.endswith('') 以什么字符结尾
print(mystr.endswith('onm'))

#3.isalpha() 是否都以字符串组成
print(mystr.isalpha()) # 字符串中间有空格
#4.isdigit 是否都以数字组成
print(mystr.isdigit())
mystr2='123456'
print(mystr2.isdigit())
#5.isalnum 都是数字或字母或数字字母的组合
print(mystr2.isalnum())
mystr3='123456aaa@'
print(mystr3.isalnum())
#isspace 都是空白返回true
print(mystr.isspace())
mystr4 = '  '
print(mystr4.isspace())