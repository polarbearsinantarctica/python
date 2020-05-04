#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 18:43
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 66-多函数之程序执行流程.py

glo_num = 0

def test1():
    global glo_num
    glo_num = 100

def test2():
    print(glo_num)

print(glo_num)
test1()
test2()
print(glo_num)