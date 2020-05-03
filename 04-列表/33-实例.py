#-*- coding: utf-8 -*-
# @Time    : 2020/5/1 3:21
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 33-实例.py
name_list = ['TOM','Lily','ROSE']
name = input('请输入您的邮箱账号名:')
if name in name_list:
    print("您输入的名字%s,此用户已经存在"%name)
else:
    print("您输入的名字%s,注册成功"%name)