#!/usr/bin/python
# -*- coding: utf-8 -*-

d = {'a': 'java', 'b': 'kotlin', 'c': 'python', 'd': 'c', 'e': 'c++'}

print(d)

# 字典默认迭代key
for key in d:
    print(key)

print()
for value in d.values():
    print(value)

print()
for k, v in d.items():
    print(k, '->', v)

# 任何可迭代对象都可以用for, 包括自定义对象
for i in 'abcdefg':
    print(i)

from collections import Iterable  # 用于判断是否是可迭代对象

print(isinstance('abc', Iterable))  # True
print(isinstance(123, Iterable))  # False

l = ['a', 'b', 'c']
for x, y in enumerate(l):  # 同时迭代list下标和元素
    print(x, y)

for m, n in enumerate(d):  # 同时迭代list下标和key
    print(m, n)

for i, j in enumerate(d.values()):  # 同时迭代list下标和value
    print(i, j)

# 不同同时迭代下标,key和value
# for x, y, z in enumerate(d.items()):
#     print(x, y, z)
