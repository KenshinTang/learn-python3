#!/usr/bin/python
# -*- coding: utf-8 -*-

list = ['java', 'kotlin', 'python', 'c', 'c++']
tuple = ('java', 'kotlin', 'python', 'c', 'c++')

print(list)
print(tuple)

print(list[1:3])
print(tuple[1:3])

print(list[-2])   # 取倒数第二个元素
print(list[-2:])  # 从倒数第二个切片
print(list[-2:-1])

print(list[::2])  # 每隔两个取一个
