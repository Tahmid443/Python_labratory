import numpy as np

# slicing numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# return [2,3,4,5]
print(np1[1:5])

#return from something till the end of the array?
print(np1[3:])

#return negative slicing
print(np1[-3:-1])

#steps
print(np1[1:5:2])

#steps on the entire array
print(np1[::2])

# slice a 2-d array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1,2])#8

print(np2[0:4,1:3])