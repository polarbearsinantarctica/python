#-*- coding: utf-8 -*-
# @Time    : 2020/4/27 22:42
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 27-字符串常用操作方法之查找.py
mystr = "hello world and itxxxx and xxwwwds and Python"

#1.find()
print(mystr.find('and'));
print(mystr.find('and',15,30));
print(mystr.find('ands'));

#2.index()
print(mystr.index('and'));
print(mystr.index('and',15,30));
#print(mystr.index('ands'));

#3.count()
print(mystr.count('and'));
print(mystr.count('and',15,30));
print(mystr.count('ands'));

#4.rfind()
print(mystr.rfind('and'));
print(mystr.rfind('and',15,30));
print(mystr.rfind('ands'));

#4.rindex()
print(mystr.rindex('and'));
print(mystr.rindex('and',15,30));
print(mystr.rindex('ands'));