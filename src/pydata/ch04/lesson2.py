import numpy as np
# m, n = (5, 3)
# x = np.linspace(0,1,m)
# y = np.linspace(0,1,n)
# X, Y = np.meshgrid(x, y)
#
# import matplotlib.pyplot as plt
# # %matplotlib inline
# plt.style.use('ggplot')
# plt.plot(X, Y, marker='.', color='blue', linestyle='none')

# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
# print(xs)
# print(ys)

arr = np.arange(9).reshape(3,3)
print(arr)
print(arr.cumsum(axis=0))
