import theano.tensor as T
from theano import function
from theano.tensor.shared_randomstreams import RandomStreams
import numpy


random = RandomStreams(seed=42)

a = random.normal((1,3))
print("a=", a)