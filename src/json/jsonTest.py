#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

d = dict(name='kenshin', age='31')
s = json.dumps(d)
print(s)

p = json.loads(s)
print(p, type(p))


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age
    }

s = Student('kenshin', 31)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
