#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random


def long_time_tast(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('process %s run %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_tast, args=(i,))
    print('waiting for all process done.')
    p.close()
    p.join()
    print('all process done')
