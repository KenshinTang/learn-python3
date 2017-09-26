#!/usr/bin/python
# -*- coding: utf-8 -*-

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 先把n-1个盘子从A借助C移到B
        move(1, a, b, c)      # 再把剩下的一个从A借助B移到C
        move(n - 1, b, a, c)  # 把B的n-1盘子从B借助A移到C

move(3, 'A', 'B', 'C')
