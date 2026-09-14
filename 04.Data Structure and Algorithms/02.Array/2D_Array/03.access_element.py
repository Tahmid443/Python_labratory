import numpy as np
twoDarr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDarr)

def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array): # O(1)
        print("Incorrect Index")  # O(1)
    else:
        print(array[rowIndex][colIndex])  # O(1)

accessElement(twoDarr,1,2)
