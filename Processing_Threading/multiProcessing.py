#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'


from multiprocessing import Process
import os

# 子进程运行的代码
def run_proc(name):
    print 'Run child process {name} : {id} ...'.format(name=name, id=os.getpid())


if __name__ == '__main__':
    print "Parent process {id}".format(id=os.getpid())
    p = Process(target=run_proc, args=('test',))
    print "Process will start"
    p.start()
    p.join()
    print "Process end."


