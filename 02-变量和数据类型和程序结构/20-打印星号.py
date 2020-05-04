#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 19:06
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 20-打印星号.py
print('---------正方形-----------')
row = 0
while row < 5:
    column = 0
    while column < 5:
        if column == 4:
            print('*', end='\n')
        else:
             print('*', end='')
        column +=1
    row +=1
print('-----------三角形-------------')
row2 = 1
while row2 < 5:
    column2 = 1
    while column2 <= row2:
        if column2 >= row2:
            print('*', end='\n')
        else:
             print('*', end='')
        column2 +=1
    row2 +=1
print('----------九九乘法表----------------')
row3 = 1
while row3 <= 9:
    column3 = 1
    while column3 <= row3:
        count3 = row3*column3
        if column3 >= row3:
            print('%dx%d=%d'%(row3,column3,count3), end='\n')
        else:
             print('%dx%d=%d'%(row3,column3,count3), end='\t') #据前面一个4个位置
        column3 +=1
    row3 +=1