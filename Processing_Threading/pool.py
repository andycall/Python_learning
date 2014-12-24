#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

from multiprocessing import Pool

import os, time, random

def long_time_task(name):
    print "The long time {name}  task : {id}".format(name=name, id=os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print "the Task {id} has sleep for {time}".format(id=os.getpid(), time=end-start)


def short_time_task(name):
    print "The short time task : {id}".format(id=os.getpid())
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print "the Task {id} has sleep for {time}".format(id=os.getpid(), time=end-start)



if __name__ == "__main__":
    print('Parent process : {id}'.format(id=os.getpid()))
    p = Pool(4) # 同时运行的子进程个数

    for i in range(10):
        p.apply_async(long_time_task, args=(i,))

    print('wait for all subProcess done')
    p.close()
    p.join()
    print('all Process done')