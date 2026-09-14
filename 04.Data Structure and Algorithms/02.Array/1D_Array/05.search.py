from array import *

arr1 = array("i", [1, 2, 3, 4, 5, 6])
arr2 = array("d", [1.3, 1.5, 1.6])

def searchArray(array, key):
    for i in array: # O(n)
        if i == key:  # O(1)
            return array.index(key) # O(n)
    return "The element does not exist in this array"  # O(n)

print(searchArray(arr1, 4))
