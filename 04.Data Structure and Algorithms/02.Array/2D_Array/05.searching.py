import numpy as np 

twoDarr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarr)

def searching(array, key):
    for i in range(len(array)): #O(mn)
        for j in range(len(array[0])): #O(m)
            if array[i][j] == key: #O(1)
                return "The value is located at row " + str(i) + " column " + str(j)
    return "The element is not found"
            
print(searching(twoDarr, 12))