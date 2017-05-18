# transpose 矩阵转置
# https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.transpose.html

import numpy as np
from termcolor import colored


x = np.arange(9).reshape((3, 3))
print(x)
print(colored('转置之后:-->', 'red'))
transpose_x = np.transpose(x)
print(transpose_x)

print('numpy.atleast_2d(*arys)[source]: -> \
    将输入视为具有至少两个维度的数组')
y = np.arange(9)
print(y)
atleast_2d_y = np.atleast_2d(y)
print(colored('atleast_2d_y:-->', 'blue'))
print(atleast_2d_y)
