#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 23:38
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 50-集合之删除.py
s1 = {10,20,30,40,40,50,50}

#1.remove()
s1.remove(10)
# s1.remove(10) #报错
print(s1)
#2.discard()
s1.discard(10)
print(s1)
#3.pop() 随机删除并返回该参数
s1.pop()
print(s1)