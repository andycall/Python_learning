#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar("0")
    except StandardError, e:
        logging.exception(e)

main()
print "END"
