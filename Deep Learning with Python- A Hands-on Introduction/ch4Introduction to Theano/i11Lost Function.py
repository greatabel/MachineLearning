import theano.tensor as T
from theano import function

a1 = T.dmatrix('a1')
a2 = T.dmatrix('a2')

f_a = T.nnet.binary_crossentropy(a1, a2).mean()
f_sigmoid = function(inputs = [a1, a2], outputs = [f_a])

print("Binary Cross Entropy [[0.01,0.01,0.01]],[[0.99,0.99,0.01]]:",
        f_sigmoid(
            [[0.01,0.01,0.01]],
            [[0.99,0.99,0.01]]
                 ) 
        )

# categroical cross entropy
b1 = T.dmatrix('b1')
b2 = T.dmatrix('b2')

f_b = T.nnet.categorical_crossentropy(b1, b2)
f_sigmoid = function([b1, b2], [f_b])

print("Categroical Cross Entropy [[0.01,0.01,0.01]],[[0.99,0.99,0.01]]:",
        f_sigmoid(
            [[0.01,0.01,0.01]],
            [[0.99,0.99,0.01]]
                 ) 
        )

# squared error
def squared_error(x, y):
    return T.sum((x - y) ** 2)

c1 = T.dmatrix('c1')
c2 = T.dmatrix('c2')

f_c = squared_error(c1, c2)
f_squared_error = function([c1, c2], [f_c])

print("Squared Error  [[0.01,0.01,0.01]],[[0.99,0.99,0.01]]:",
        f_squared_error(
            [[0.01,0.01,0.01]],
            [[0.99,0.99,0.01]]
                 ) 
        )