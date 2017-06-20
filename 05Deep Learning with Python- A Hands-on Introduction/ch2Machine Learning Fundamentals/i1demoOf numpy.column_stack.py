# https://docs.scipy.org/doc/numpy/reference/generated/numpy.column_stack.html

import numpy as np
from numpy.linalg import inv


a = np.array((1,2,3))
b = np.array((10,20,30))
c = np.column_stack((a, b))
print('column_stack:', c)

print('power:')
x1 = range(6)
for i in x1:
    print('i=', i)
degree = 2
for i in range(0, degree):
    print(np.power(x1,i))

combined = np.column_stack([np.power(x1,i) for i in range(0, degree)])
print('combined = ', combined)

print('逆矩阵')
a = np.array([[1., 2.], [3., 4.]])
ainv = inv(a)
print(a,'\n', ainv)