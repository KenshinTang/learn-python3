#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('process to write: %s' % os.getpid())
    for v in ['a', 'b', 'c']:
        print('put %s to queue' % v)
        q.put(v)
        time.sleep(random.random())


def read(q):
    print('process to read: %s' % os.getpid())
    while True:
        v = q.get(True)
        print('get %s from queue' % v)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
