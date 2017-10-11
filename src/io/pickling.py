#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
i = (1, 2, 3, 4, '5')
print(pickle.dumps(i))

f = open('dump.txt', 'wb')
pickle.dump(i, f)
f.close()

f = open('dump.txt', 'rb')
x = pickle.load(f)
f.close()
print(x)
