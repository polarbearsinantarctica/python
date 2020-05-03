#-*- coding: utf-8 -*-
# @Time    : 2020/5/1 3:27
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 34-列表之增加.py
name_list = ['TOM','Lily','ROSE']
#1.append
name_list.append('LiSi')
name_list.append([11,22])
print(name_list)
#2.extend 拆开之后追加
name_list.extend('LiSi')
name_list.extend([11,22])
print(name_list)
#3.insert 指定位置新增数据
name_list.insert(1,'haha')
print(name_list)