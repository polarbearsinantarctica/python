#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 18:28
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 17-while循环.py
num = 1
while num <= 99:
    print(num)
    num +=1 # 先+,后赋值
    print('我错了%d' %num)
num2 = 1
count = 0
while num2 <= 100:
    count = count + num2
    num2 +=1
print(count)

evenNum = 1
evenCount = 0
while evenNum <= 100 :
    if (evenNum%2) == 0:
        evenCount = evenCount + evenNum
    evenNum +=1
print(evenCount)