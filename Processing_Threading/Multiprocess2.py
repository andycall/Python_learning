#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'


from multiprocessing import Process
import os, time, random

def r1(process_name):
    for i in range(5):
        print 'the process name {name} and pid : {pid}'.format(name=process_name, pid=os.getpid())
        time.sleep(random.random())


def r2(process_name):
    for i in range(5):
        print 'the process name {name} and pid : {pid}'.format(name=process_name, pid=os.getpid())
        time.sleep(random.random())



if __name__ == '__main__':
    print "Main Process run:"
    p1 = Process(target=r1, args=('process1',))
    p2 = Process(target=r2, args=('process2',))

    p1.start()
    p2.start()
    p1.join() # 阻塞当前进程， 直到p1 运行完
    p2.join() # 阻塞当期进程， 知道p2 运行完
    print "main process runned all lines"

