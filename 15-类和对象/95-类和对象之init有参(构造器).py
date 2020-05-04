#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:28
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 95-面向对象之init有参(构造器).py
class Washer():
    def __init__(self,width,height): #自动调用，创建对象时调用 (java的构造器)
        print('init方法，实例化对象时调用')
        self.width = width
        self.height = height
    def info(self):
        print(self.width) #内调用
        print(self.height)

haier1=Washer(600,700)
haier1.info()
haier2=Washer(800,900)
haier2.info()