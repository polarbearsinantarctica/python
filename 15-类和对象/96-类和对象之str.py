#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:32
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 96-面向对象之str.py
class Washer():
    def __init__(self,width,height): #自动调用，创建对象时调用 (java的构造器)
        print('init方法，实例化对象时调用')
        self.width = width
        self.height = height
    def __str__(self): # 打印实例化对象时调用(java的string方法) 不格式化默认输出内存地址
        return 'str方法，实例化对象时调用'+str(self.width)
    def info(self):
        print('info方法，实例化对象调用时调用')
haier1=Washer(500,600)
print(haier1)