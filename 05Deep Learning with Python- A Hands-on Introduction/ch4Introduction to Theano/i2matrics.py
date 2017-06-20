import numpy as np
import theano.tensor as T
from theano import function

from termcolor import colored

a = T.dmatrix('a')
b = T.dmatrix('b')
c = T.dmatrix('c')
d = T.dmatrix('d')

e = (a + b - c) * d

f = function([a, b, c, d], e)

a_data = np.array([
    [1,1],
    [1,1]
    ])
b_data = np.array([
    [2,2],
    [2,2]
    ])
c_data = np.array([
    [5,5],
    [5,5]
    ])
d_data = np.array([
    [3,3],
    [3,3]
    ])

print("Expected:", (a_data + b_data - c_data) * d_data)
print(colored('*'*25, 'red'))
print("Via Theano:", f(a_data, b_data, c_data, d_data))