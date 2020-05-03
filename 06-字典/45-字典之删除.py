#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 22:51
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 45-字典之删除.py
dict1={'name': 'Tom','age':20,'gender': '男'}

#1.del删除字典或删除指定键值对
#del(dict1)
#print(dict1)

del dict1['name'] # 不能删除不存在的key
print(dict1)
#2.clear 清空字典

dict1.clear()
print(dict1)
