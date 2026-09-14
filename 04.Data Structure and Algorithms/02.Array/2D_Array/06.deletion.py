import numpy as np

twoDarr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarr)
print(" ")
#Time complexity O(mn)
newArr = np.delete(twoDarr, 0, axis = 0) # 0 row delete
newArr = np.delete(twoDarr, 0, axis = 1) # 0 column delete
print(newArr)