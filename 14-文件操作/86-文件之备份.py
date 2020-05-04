#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 12:57
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 86-文件之备份.py
old_name=input('请输入您要备份的文件名')
#print(old_name)
index=old_name.rfind('.')
if index>0:
    postfix=old_name[index:]
new_name=old_name[:index] + '[备份]'+postfix
old_f=open(old_name,'rb')
new_f=open(new_name,'wb')
while True:
    con=old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)
new_f.close()
old_f.close()