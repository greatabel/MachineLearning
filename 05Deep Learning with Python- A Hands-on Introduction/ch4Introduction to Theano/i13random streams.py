import theano.tensor as T
from theano import function
from theano.tensor.shared_randomstreams import RandomStreams
import numpy


random = RandomStreams(seed=42)

a = random.normal((1,3))
b = T.dmatrix('a')

f1 = a * b

g1 = function([b], f1)

print('numpy.ones((1,3)=', numpy.ones((1,3)))
print('numpy.ones((1,3)=', numpy.ones((1,3)))
print('numpy.ones((1,3)=', numpy.ones((1,3)))

for i in range(50):
    print("Invocation 1:", g1(numpy.ones((1,3))) )


