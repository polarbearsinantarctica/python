#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 3:40
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 82-文件之模式特点.py

#r 文件存在，正常打开；文件不存在，保存。
f=open('test.txt','r')
print(f.read())
f.close()
#w 文件存在，正常打开；文件不存在，创建文件。
f=open('test.txt','w')
f.write('bbb\n') #覆盖重写
f.close()
#a 文件存在，正常打开；文件不存在，创建文件。
f=open('test.txt','a')
f.write('aaa\nbbb\nccc')# 追加新内容
f.close()

#访问模式省略 默认值是 r
f=open('test.txt')
print(f.read())
f.close()

#派生模式遵循主模式的特点  以下r,w文件指针都在开头
# r rb r+ rb+ 只要文件不存在，都报错 rb为二进制方式只读  (指针在文件开头)
# w wb w+ wb+ 文件不存在，则创建 ；文件存在，则重新写入  (指针在文件开头)
# a ab a+ ab+  文件不存在，则创建；文件存在，则追加写入  追加 (指针在文件结尾) (a的指针在结尾，读取为空)