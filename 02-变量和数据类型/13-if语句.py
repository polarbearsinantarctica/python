#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 17:53
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 13-if语句.py
if 1 == 2:
    print('执行1');
    print('执行2');
print('执行3');

# 上网实例
message = input('请输入您的年龄\n');
if int(message) > 18:
    print('欢迎上网');
elif int(message) == 18:
    print('您暂时不可以上网');
else:
    print('您当前还不能上网');
