#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)


    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' Object has no attribute %s" % item)

    def __setattr__(self, key, value):
        self[key] = value


