#!/usr/bin/python
#-- coding:utf-8 --
#这是一个尾递归
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
#都只占用一个栈帧，不会出现栈溢出的情况。
#但是python没有优化,所以还是会溢出
def x(n):
    return x1(n, 1)

def x1(num, product):
    if num == 1:
        return product
    return x1(num-1, num*product)

n = input()
print(x(int(n)))
input()
