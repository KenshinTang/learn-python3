#!/usr/bin/python
# -*- coding: utf-8 -*-


# 函数作为另一个函数的参数. 高阶函数
def high_order_func(x, y, f):
    return f(x) + f(y)


print(high_order_func(-1, 1, abs))
