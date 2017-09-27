#!/usr/bin/python
# -*- coding: utf-8 -*-

L = [x * x for x in range(1, 11)]
print(L)

g = (x * x for x in range(1, 11))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

fib(10)


def fib_g(max):
    n, a, b = 0, 0,1
    while n < max:
        yield
        a, b = b, a + b
        n += 1
    return 'done'

print()

f = fib(6)
next(f)
