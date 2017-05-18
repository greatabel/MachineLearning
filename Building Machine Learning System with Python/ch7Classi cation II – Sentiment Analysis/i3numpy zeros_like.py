# https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.zeros_like.html
import numpy as np
x = np.arange(6)
x = x.reshape((2, 3))
print(x)
zero_x = np.zeros_like(x)
print(zero_x)
