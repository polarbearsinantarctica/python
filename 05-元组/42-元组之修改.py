#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 16:30
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 42-元组之修改.py
#t1 = (10,20,30,30,40)

# 不支持修改
#t1[t1.index(10)] = 222

t2 = ('aa',['bb','cc'],'dd')
#t2[1] = ['ee']
print(t2)
t2[1][0] = ['ff']
print(t2)