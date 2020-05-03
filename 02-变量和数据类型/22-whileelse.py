#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 21:49
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 22-whileelse.py
i = 1
while i <= 5:
    print('我错了')
    i +=1
    1/0
else:
    print('没关系') # 它和while是一个整体，break时、异常终止时不执行，continue时执行