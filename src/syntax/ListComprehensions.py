#!/usr/bin/python
# -*- coding: utf-8 -*-


def println(*args):
    print(args, '\n')


# 通过range生成列表
l = list(range(1, 11))
println(l)

ll = [x * x for x in range(1, 11)]
println(ll)

lll = [x * x for x in range(1, 11) if x % 2 == 0]
println(lll)

list1 = [m + n for m in 'abc' for n in 'xyz']
print(list1)

list2 = [m + str(n) for m in 'abc' for n in range(1, 4)]
print(list2)

# 列出当前目录下所有的文件
import os

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '->' + v for k, v in d.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
L3 = [x.upper() for x in L1 if isinstance(x, str)]
print(L2)
print(L3)
