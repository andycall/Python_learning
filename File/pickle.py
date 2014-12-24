#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

# 序列化

try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='andycall', age=18, score=88)

# 一般序列化
def normal_pickle():
    print pickle.dumps(d)

# 直接写入文件中去
def write_pickle():
    with open("pickle/dump.txt", 'wb') as f:
        pickle.dump(d, f)

# 从文件中读出数据
def read_pickle():
    with open("pickle/dump.txt", 'r') as f:
        print pickle.load(f)



read_pickle()

