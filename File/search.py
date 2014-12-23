#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

import os

now_path = os.path.abspath(".")

def find(path, str):

    if not os.path.exists(path):
         return

    dir_list = os.listdir(path)

    for dir in dir_list:
        new_path = os.path.join(path, dir)
        if os.path.isdir(new_path):
            find(new_path, str)
        else:
            with open(new_path, 'r') as f:
                if str in f.read():
                    print new_path



print find(now_path, 'Helloworld')