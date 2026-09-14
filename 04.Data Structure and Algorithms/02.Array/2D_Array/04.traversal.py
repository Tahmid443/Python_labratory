import numpy as np

twoDarr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarr)

def traverseArray(array):
    for i in range(len(array)): #O(mn)
        for j in range(len(array)): #O(n)
            print(array[i][j]) #O(1)
            
traverseArray(twoDarr)