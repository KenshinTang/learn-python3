#!/usr/bin/python
# -*- coding: utf-8 -*-


def log(func):
    def wrapper(*args, **kw):
        print(func.__name__, 'enter')
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2017.9.29')


now()

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(func.__name__, 'enter')
            func(*args, **kw)
            print(func.__name__, 'exit')
            return func

        return wrapper

    return decorator


@log('exec')
def now():
    print('2017.9.29')

now()
