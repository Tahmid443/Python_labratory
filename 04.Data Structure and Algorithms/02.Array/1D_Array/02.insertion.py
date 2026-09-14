#Insertion at the end of the array(time complexity: O(1))
#Insertion to full array(time complexity: O(n))
from array import *
arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.3,1.5,1.6])

print(arr2)

arr1.insert(6,7)#inserting 7 in 6th index
print(arr1)
arr1.insert(0,10)#inserting 10 in first position and expand the size as well
print(arr1)