#-*- coding: utf-8 -*-
# @Time    : 2020/4/30 23:32
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 29-字符串常用操作方法之修改之非重点.py

mystr = "hello world and itxxxx and xxwwwds and Python"
#1.capitalize() 整个字符串的首字母大写
new_str = mystr.capitalize()
print(new_str)
#2.title() 字符串中每个单词的首字母大写
new_str = mystr.title()
print(new_str)
#3.upper() 小写转大写
new_str = mystr.upper()
print(new_str)
#4.lower() 大写转小写
new_str = mystr.lower()
print(new_str)

mystr = " hello world and itxxxx and xxwwwds and Python "
print(mystr)
#1.lstrip() 删除字符串左侧空白
new_str = mystr.lstrip()
print(new_str)
#2.rstrip() 删除字符串右侧空白
new_str = mystr.rstrip()
print(new_str)
#3.strip() 删除字符串左、右侧空白
new_str = mystr.strip()
print(new_str)

