#!/usr/bin/python
# -*- coding: utf-8 -*-


# 把一个函数作用在一个Iterable上
def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

s = map(str, [1, 2, 3, 4, 5])
print(list(s))
