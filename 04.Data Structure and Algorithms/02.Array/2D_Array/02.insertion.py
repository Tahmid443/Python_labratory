import numpy as np
twoDarr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarr)

newTwoDArr = np.insert(twoDarr, 1, [[1,2,3,4]], axis = 0) #insert(array, index, new array, axis = (if 0 insert in row, if 1 insert in column))
print(newTwoDArr)

newTwoDArr = np.append(twoDarr, [[1,2,3,4]], axis = 0) #append in the last row
print(newTwoDArr)

