#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 17:21
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 93-面向对象之对象属性(内).py

#2.对象属性在内操作
class Washer():
    width = 500 #类中定义属性
    height = 600
    def wash(self):
        print('-' * 10 + '对象属性内获取' + '-' * 10)
        print(self.width)
        print(self.height)
        print('wash函数')
    def info(self):
        print('-' * 10 + '对象属性内获取' + '-' * 10)
        print(self.no) #获取未添加的属性报错
        print('info函数')

haier1=Washer()
print('-'*10+'对象属性外获取'+'-'*10)
haier1.width=700
print(haier1.width)
print(haier1.height)
haier1.wash()
haier1.info()