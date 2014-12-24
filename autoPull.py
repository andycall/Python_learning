#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

import subprocess, os, logging


def checkIfGit(str):
    if '.git' in str and os.path.isdir(str):
        return True
    else:
        return False

paths = []

def find(path):
    if not os.path.exists(path):
        return

    dir_list = os.listdir(path)

    for dir in dir_list:
        new_path = os.path.join(path, dir)
        if(checkIfGit(new_path)):
            paths.append(new_path.replace('/.git', ''))
        else:
            if os.path.isdir(new_path):
                find(new_path)

def RunPull(paths):
    now_path = os.path.abspath('.')

    for i in paths:
        name = i.split('/')[-1]
        try:
            os.chdir(i)
            now_branch = subprocess.check_output(['git', 'branch']).split(' ')[-1].strip('\n')
            now_origin = subprocess.check_output(['git', 'remote']).strip('\n')
            output = subprocess.check_output(['git', 'pull', now_origin, now_branch])
            with open(now_path + '/log/{name}.log'.format(name=name), 'wb') as f:
                f.write("---------- " + name + '------------\n' + output + '\n')
        except subprocess.CalledProcessError, e:
            logging.exception(e)
            with open(now_path + '/log/error.log', 'wb') as f:
                f.write("Failed :" + name + '\n' + e + '\n')

if __name__ == "__main__":

    now_path = os.path.abspath(".")
    find(now_path)
    path_length = len(paths)
    RunPull(paths)