import numpy as np
# a = np.arange(10)
# np.save('d:/a', a)
#
# print(np.load('d:/a.npy'))

# import random
# position = 0
# walk = [position]
# steps = 1000
# for i in range(1000):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
# print(walk)

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
# print(steps)
walk = steps.cumsum()
# print(walk)
print(walk.min())
print(walk.max())
print((np.abs(walk) >= 10).argmax())
for index, item in enumerate(np.abs(walk) >= 10):
    if item:
        print(index)
        break

