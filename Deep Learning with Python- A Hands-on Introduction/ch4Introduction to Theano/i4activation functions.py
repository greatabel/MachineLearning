import theano.tensor as T
from theano import function

#sigmod
'''
S(x) = 1/(1 + e^-x)
'''
a = T.dmatrix('a')
f_a = T.nnet.sigmoid(a)
f_sigmoid = function([a],[f_a])

print("sigmod:", f_sigmoid([[-1, 0, 1]]) )

# tanh
'''
tanh = e^x - e^-x / (e^x + e^-x)
'''

b = T.dmatrix('b')
f_b = T.tanh(b)
f_tanh = function([b],[f_b])
print("tanh:", f_tanh([[-1,0,1]]))

# fast sigmoid
c = T.dmatrix('c')
f_c = T.nnet.ultra_fast_sigmoid(c)
f_fast_sigmoid = function([c], [f_c])
print("fast sigmoid:", f_fast_sigmoid([[-1,0,1]]))

# softplus
d = T.dmatrix('d')
f_d = T.nnet.softplus(d)
f_softplus = function([d],[f_d])
print( "soft plus:",f_softplus([[-1,0,1]]) )

# relu
e = T.dmatrix('e')
f_e = T.nnet.relu(e)
f_relu = function([e],[f_e])
print("relu:",f_relu([[-1,0,1]]) )

# softmax
f = T.dmatrix('f')
f_f = T.nnet.softmax(f)
f_softmax = function([f],[f_f])
print("soft max:",f_softmax([[-1,0,1]]))