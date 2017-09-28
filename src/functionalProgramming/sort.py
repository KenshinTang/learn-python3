#!/usr/bin/python
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(m):
    return m[0]


def by_score(n):
    return n[1]


L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
print(L2)
print(L3)
