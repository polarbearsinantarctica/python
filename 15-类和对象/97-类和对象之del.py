#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:39
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 97-面向对象之del.py
class Washer():
    def __init__(self): #自动调用，创建对象时调用 (java的构造器)
        print('init方法，实例化对象时调用')
    def __del__(self):
        print('del方法，删除实例化对象时调用')
haier1=Washer()

#del haier1 解释器自动结束程序，删除对象