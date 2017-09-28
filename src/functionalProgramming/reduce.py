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


def fx(x, y):
    return x * y


def prod(L):
    return reduce(fx, L)


print('1*2*3*4=', prod([1, 2, 3, 4, 2]))


def f2(x, y):
    return x * 0.1 + y


def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def fm(x, y):
        return x * 0.1 + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    s1 = s[:s.index('.')]
    x = reduce(fn, map(char2num, s1))
    print(x)

    s2 = s[s.index('.')+1:]
    s3 = s2[::-1]
    y = reduce(fm, map(char2num, s3)) * 0.1
    print(y)
    return x + y


print('str2float(\'123.456\') =', str2float('1233.885677'))
