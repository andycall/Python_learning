#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

import os

# OS name
print os.name
# detail name
print os.uname()


# 环境变量
print os.environ


# 获取环境变量
print os.getenv("PATH")

# 获取当前目录的绝对路径
now_path =  os.path.abspath(".")

## 在某个目录下创建一个新的目录
# start

# 表示出一个完成路径
path = os.path.join(os.path.abspath("."), "test")

# 创建一个目录
os.mkdir(path)

# 删除一个目录
# os.rmdir(path)

# 拆分路径
os.path.split(path, "test")

# 获取扩展名
os.path.splitext(os.path.abspath("."))

# 对文件重命名
#






# end






