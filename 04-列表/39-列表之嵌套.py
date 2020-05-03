#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 16:04-列表
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 39-列表之嵌套.py
name_list = [['小明','小红','小绿'],['Tom','Lily','Rose'],['张三','李四','王五']]

for i in name_list:
    for j in i:
        print(j)