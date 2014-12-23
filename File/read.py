#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'


# Read Config File
with open("../.gitignore", 'r') as f:
    for line in f.readlines():
        print(line.strip())


# Read Binary File
with open("./QQ20141207-1.png", 'rb') as f:
    print(f.read())


# Read GBK File

with open("./GBK.txt", 'rb') as f:
    u = f.read().decode('gbk')
    print u

