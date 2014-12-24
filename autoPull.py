#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

from multiprocessing import Process, Pool
import os, time, random


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
            paths.append(new_path.replace('.git', ''))
        else:
            if os.path.isdir(new_path):
                find(new_path)
            # else:
            #     with open(new_path, 'r') as f:
            #         if str in f.read():
            #             print new_path


def Pull(path, index):
    print 'Running {index} of {total}'.format(index=index, total=path_length)

    # log = os.popen('git pull ' + path).read()
    name = path.split('/')[-2]

    print name

    if not os.path.exists(now_path + 'log'):
        os.mkdir(now_path + 'log')

    with open(os.path.join(now_path, 'log/{index}.log'.format(index=index)), 'wb') as f:
        f.write(log)


def RunPull(paths):
    p = Pool(4)
    # print(paths)

    for i in range(len(paths)):
        p.apply_async(Pull, args=(paths[i], i))

    print('Wait for all subProcess done')
    p.close()
    p.join()
    print("All work Done")


if __name__ == "__main__":

    now_path = os.path.abspath(".")
    find(now_path)
    path_length = len(paths)
    RunPull(paths)