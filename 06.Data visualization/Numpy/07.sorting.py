import numpy as np

# np.sort() 1-d numeric

np1 = np.array([6,7,4,9,0,2])
print(np.sort(np1))

# Alphabetical
np2 = np.array(["Tahmid", "Dhrubo", "Taqi"])
print(np.sort(np2))

# booleans
np3 = np.array([True, False, False, True])
print(np3)
print(np.sort(np3))

# return a copy not change the original
print(np1)
print(np.sort(np1))
print(np1)

# 2-d
np4 = np.array([[6,7,1,9],[8,3,5,2]])
print(np.sort(np4))