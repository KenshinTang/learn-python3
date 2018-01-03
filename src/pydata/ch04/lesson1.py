import numpy as np
# data = np.random.randn(2, 3)
# # print(data)
# # print(data.shape)
# # print(data.dtype)
#
# list1 = [1, 2, 3, 4]
# list2 = [[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
# print(np.array(list1))
# print(np.array(list2))
# print(np.array(list2).dtype)
# print(np.array(list2).shape)
# print(type(np.arange(10)))

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names == 'Bob')
data = np.random.randn(7,4)
print(data[names == 'Bob'])
print(data[names == 'Bob', 3])
