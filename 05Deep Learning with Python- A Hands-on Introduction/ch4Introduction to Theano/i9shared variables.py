import theano.tensor as T
from theano import function
from theano import shared

import numpy
x = T.dmatrix('x')
y = shared(numpy.array([[4, 5, 6]])) 
z = x + y
f = function(inputs = [x], outputs = [z])
print("Original Shared Value:", y.get_value())
print("Original Function Evaluation:", f([[1, 2, 3]]) )

y.set_value(numpy.array([[5, 6, 7]]))
print("Original Shared Value:", y.get_value())
print("Original Function Evaluation:", f([[1, 2, 3]]) )
