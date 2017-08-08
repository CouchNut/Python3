#!/usr/local/bin python3

# -*- coding: utf-8 -*-


print('---------- 操作文件和目录 ----------')
import os
# 查看当前目录的绝对路径
pwd = os.path.abspath('.')
print(pwd)

# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(s)])



































































