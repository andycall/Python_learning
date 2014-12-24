#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

import time, threading

# 新线程执行的代码
def loop():
    print("Threading running: {name}".format(nam=threading.current_thread().name))

    for i in range(5):
        print('Threading {name} >>> {index}'.format(name=threading.current_thread().name, index=i))
        time.sleep(1)

    print('thread {name} ended'.format(name=threading.current_thread().name))


print('threading {name} is running'.format(name=threading.current_thread().name))
t = threading.Thread(target=loop, name='Threadloop')
t.start()
t.join()
print('threading {name} ended'.format(name=threading.current_thread().name))
