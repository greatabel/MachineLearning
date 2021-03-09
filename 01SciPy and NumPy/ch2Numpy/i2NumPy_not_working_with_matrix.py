import numpy as np

arr = np.zeros((3,3,3,3))
print(arr)

# Trying to convert array to a matrix, which will not work 
mat = np.matrix(arr)
# "ValueError: shape too large to be a matrix."