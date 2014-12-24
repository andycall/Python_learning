#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

from multiprocessing import Process, Queue

import os, time, random

# 用于写的进程

def write_process(q):
    for value in ['A', 'B', 'C']:
        print('put {value} into queue'.format(value=value))
        q.put(value)
        time.sleep(random.random())


# 用于读的进程
def read_process(q):
    while True:
        value = q.get(True)
        print 'Get {value} from queue'.format(value=value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write_process, args=(q,))
    rw = Process(target=read_process, args=(q,))


    pw.start()
    rw.start()

    pw.join()
    rw.terminate()

