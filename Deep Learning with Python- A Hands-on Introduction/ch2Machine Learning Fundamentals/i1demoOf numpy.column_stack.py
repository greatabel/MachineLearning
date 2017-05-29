# https://docs.scipy.org/doc/numpy/reference/generated/numpy.column_stack.html

import numpy as np

a = np.array((1,2,3))
b = np.array((10,20,30))
c = np.column_stack((a, b))
print(c)