#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 21:31
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 73-函数之实例运用.py
def info_print():
    print('请选择功能')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')

info=[]

def add_info():
    """添加学员"""
    new_id=input('请输入学号')
    new_name=input('请输入姓名')
    new_tel=input('请输入手机号')

    global info

    for i in info:
        if i['name'] == new_name:
            print('用户存在，重名了')
            return
    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    info.append(info_dict)
    print(info)
    #pass #代码不知道写什么，可以先占位
def del_info():
    """删除学员"""
    global info
    print(info)
    del_name=input('请输入要删除的学员姓名')
    j=0
    #奇怪现象，边循环边删除 js中不可以
    for i in info:
        if del_name==i['name']:
            info.remove(i)
            break
    else: #从头到尾都遍历了，则执行
        print('学员不存在')
    print(info)
def modify_info():
    """修改学员"""
    modify_name = input('请输入要修改的学员姓名')
    global info
    for i in info:
        if i['name']==modify_name:
            i['tel']=input('请输入新的手机号')
            break
    else:
        print('学员不存在')
    print(info)
def print_all():
    """显示所有学员信息"""
    print('学员\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")
def search_info():
    """查询学员"""
    search_name=input('请输入要查找的学员姓名')
    global info
    for i in info:
        if search_name==i['name']:
            print(f"该学员的学号是{i['id']}，姓名是{i['name']}，手机号是{i['tel']}")
            break
    else:
        print('该学员不存在')
user_num = 0
while user_num >=0 and user_num != 6:
    info_print()
    user_num = int(input('请输入功能序号\n'))
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        print('退出当前系统')
    else:
        print('输入有误')