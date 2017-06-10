import theano.tensor as T
from theano import function

a1 = T.dmatrix('a1')
a2 = T.dmatrix('a2')

f_a = T.nnet.binary_crossentropy(a1, a2).mean()
f_sigmoid = function(inputs = [a1, a2], outputs = [f_a])

print("Binary Cross Entropy [[0.01,0.01,0.01]],[[0.99,0.99,0.01]]:",
        f_sigmoid(
            [[0.01,0.01,0.01]],[[0.99,0.99,0.01]]) 
        )