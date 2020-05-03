#-*- coding: utf-8 -*-
# @Time    : 2020/4/27 22:55
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 28-字符串常用操作方法之修改.py
mystr = "hello world and itxxxx and xxwwwds and Python" #字符串为不可变数据类型

#1.replace() 替换
print(mystr.replace('and','he')) #返回的结果是替换后的字符串，不操作原始字符串 替换次数可以超出

#2.split() 分隔 返回的是一个列表
print(mystr.split(' ',10))

#join() 合并列表中的字符串为一个大字符串
mylist = ['hello', 'world', 'and', 'itxxxx', 'and', 'xxwwwds', 'and', 'Python'];
print(' '.join(mylist))