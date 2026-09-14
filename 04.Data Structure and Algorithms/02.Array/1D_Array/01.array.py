# array can store data of specific type
# elements of array are located in a contigious
# each element of array has a unique index
# size of an array is predefined and cannot be modified
"""
There are two types of array
1. One dimensional: an array with a bunch of values having been declared with a single index; a[index] 
2. Multi dimensional: an array eith a bunch of values having declared with double index; a[row index][col index]
"""
"""
Creating an array

when we create an array, we:
1.Assign it to variable
2.Define the type of elements that it will store
3.Define its size
"""
"""
Code       Python Type           Min bytes
'b'                int                   1
'B'                int                   1
'u'            unicode                   2
'h'                int                   2
'H'                int                   2
'i'                int                   2
'I'                int                   2
'l'                int                   4
'L'                int                   4
'f'              float                   4
'd'              float                   8

"""
from array import *

arr1 = array('i',[1,2,3,4,5])
print(arr1)