import theano.tensor as T
from theano import function

#sigmod
a = T.dmatrix('a')
f_a = T.nnet.sigmoid(a)
f_sigmoid = function([a],[f_a])

print("sigmod:", f_sigmoid([[-1, 0, -1]]) )