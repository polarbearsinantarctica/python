#-*- coding: utf-8 -*-
# @Time    : 2020/4/24 23:39
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 05-元组-格式化输出.py
age = 18
name = 'TOM'
weight = 75.5
stu_id = 1

print('今年我的年龄是%d岁'% age)

print('我的名字是%s'% name)

print('我的体重是%.2f公斤'% weight) # .位数

print('我的学号是%d' %stu_id)

print('我的学号是%03d' % stu_id) # 补全

print('我的名字%s是,今年%d岁了'%(name,age))

print('我的名字%s是,名年%d岁了'%(name,age+1))