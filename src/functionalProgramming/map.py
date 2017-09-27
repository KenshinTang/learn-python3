#!/usr/bin/python
# -*- coding: utf-8 -*-


# 把一个函数作用在一个Iterable上
def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

s = map(str, [1, 2, 3, 4, 5])
print(list(s))


def normalize(name):
    s = ''
    for index, char in enumerate(name):
        print(index, char)
        if index == 0:
            s += name[index].upper()
        else:
            s += name[index].lower()
    return s


def normalize1(name):
    s = ''
    for char in name:
        i = name.index(char)
        if i == 0:
            s += name[i].upper()
        else:
            s += name[i].lower()
    return s


def normalize2(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize2, L1))
print(L2)
