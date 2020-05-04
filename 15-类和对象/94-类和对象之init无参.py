#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:19
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 94-面向对象之init无参.py
class Washer():
    def __init__(self): #自动调用，创建对象时调用 (java的构造器)
        print('init方法，实例化对象时调用')
        self.width = 500 #类中定义属性
        self.height = 600
        print(self.width)
    def wash(self):
        print(self.width) #内调用
        print(self.height)
haier1=Washer()
haier1.wash()
print(haier1.width) #外调用