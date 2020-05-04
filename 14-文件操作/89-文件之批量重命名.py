#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 15:12
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 89-文件之批量重命名.py
import os
list1 = [
    'a','b','c','d','e',
    'f','g','h','i','j',
]
#切换目录
#os.mkdir('aa')
os.chdir('./aa')
# for i in list1:
#     os.mkdir(i)
file_list = os.listdir()
print(file_list)
flag=2
for i in file_list:
    if flag == 1:
        new_name='Python_'+i
    elif flag == 2:
        num = len('Python_')
        new_name = i[num:]
    os.rename(i, new_name)