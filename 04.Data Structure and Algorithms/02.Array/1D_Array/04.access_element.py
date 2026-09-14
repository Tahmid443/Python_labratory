from array import *

arr1 = array("i", [1, 2, 3, 4, 5, 6])
arr2 = array("d", [1.3, 1.5, 1.6])

def accessElement(array, index):
    if index >= len(array): #O(1)
        print("There is not any element in this index")  # O(1)
    else: 
        print(array[index])  # O(1)

accessElement(arr1, 60)
