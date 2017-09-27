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
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        yield
        a, b = b, a + b
        n += 1
    return 'done'


print()

f = fib_g(6)
next(f)
next(f)
next(f)
next(f)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
def triangles():
    a = 1
    b = 1
    
    return [1]


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break