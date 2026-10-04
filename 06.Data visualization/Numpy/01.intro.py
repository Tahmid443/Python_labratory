import numpy as np

list1 = [1,2,3,4,5]
# print(list1)

list2 = ['Tahmid', 43, 4.98, False]
# print(list2)

# Numpy - Numeric Python
# ndarray - n-dimensional array
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

# shape
print(np1.shape)

# range
np2 = np.arange(10)
print(np2)
np3 = np.arange(0,10,2)
print(np3)

# zeros
np4 = np.zeros(10)
print(np4)

# multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

#full
np6 = np.full((10),6)
np7 = np.full((2,10),6)
print(np6)
print(np7)

# convert python list to numpy
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)