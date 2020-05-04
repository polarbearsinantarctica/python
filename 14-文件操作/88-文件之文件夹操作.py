#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 14:54
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 88-文件之文件夹操作.py
import os
#1.mkdir() 创建文件夹
#os.mkdir('aa')
#2.rmdir() 删除文件夹
#os.rmdir('aa.txt')
#3.getcwd()获取当前目录 获取的是绝对路径
#print(os.getcwd())
#4.chdir() 改变当前文件的默认目录
#os.chdir('aa') # cd 命令
    #在aa中创建bb
#os.mkdir('bb')
#5.listdir 获取某个文件夹下的所有文件(包含文件夹)，返回结果是列表
#os.chdir('../../') #类似shell命令的切换都可以
#print(os.listdir('PythonBasicCode'))
#6.rename 重命名文件夹
#os.chdir('./aa')
#os.rename('bb','cc')