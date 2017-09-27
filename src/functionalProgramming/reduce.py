#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce


def f(x, y):
    return x + y


r = reduce(f, [1, 2, 3, 4, 5])
print(r)


def f1(x, y):
    return x * 10 + y


print(reduce(f1, [1, 2, 3, 4, 5]))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    return reduce(fn, map(char2num, s))


print(str2int('635743'))
