#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

import json

d = dict(name='andycall', age=18, score=99)

def print_json():
    print json.dumps(d)

def write_json():
    with open("pickle/json.txt", 'wb') as f:
        json.dump(d,f)

def read_json():
    with open("pickle/json.txt", 'r') as f:
        print(f.read())

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def studentConver(self):
        return {
            'name' : self.name,
            'age'  : self.age,
            'score': self.score
        }

def CoverObjectToJson(obj):
    print json.dumps(obj, default=Student.studentConver)

def CoverObjectToJson_2(obj):
    print json.dumps(obj, default=lambda obj: obj.__dict__)




s = Student('andycall', 18, 88)

# print json.dumps(s, default=Stu)
# CoverObjectToJson_2(s)

print lambda s : s.__dict__