#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_palindrome(n):
    s = str(n)
    print(s, "".join(reversed(s)))
    return s == s[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))
