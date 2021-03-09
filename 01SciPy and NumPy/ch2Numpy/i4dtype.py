import numpy as np

arr = np.zeros(2, dtype=int)
print('1 arr=', arr)

arr = np.zeros(2, dtype=np.float32)
print('2 arr=', arr)

# Creating an array with elements from 0 to 999 
arr1d = np.arange(8)
print('3 arr=', arr1d)

# Now reshaping the array to a 10x10x10 3D array 
arr3d = arr1d.reshape((2,2,2))
print('4 arr=', arr3d)

# The reshape command can alternatively be called this way 
arr3d = np.reshape(arr1d, (2, 2, 2))
print('5 arr=', arr3d)
# Inversely, we can flatten arrays 
arr4d = np.zeros((2, 2, 2, 2)) 
print('6 arr4d=', arr4d)
arr1d = arr4d.ravel()
print('7 shape=',arr1d.shape )

print('-' * 10)
print(np.zeros((4,3,2)))
print('#' * 10)
print(np.zeros((2,3,4)))

