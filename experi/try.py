# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Brisky
@Version        :  WIN10, Python3.7.9
------------------------------------
@IDE            ： PyCharm-> try.py
@Description    :  
@CreateTime     :  2022/12/23 22:28
------------------------------------
"""
# enumerate从1开始更加human
# 尝试enumerate的start 参数
# for index,value in enumerate(range(10),1):
#     print(f'{index}, {value}')
# 尝试列表生成式双层循环
a = [[] for i in range(10)] # 大列表套着小列表,形成二维矩阵
print(a)
