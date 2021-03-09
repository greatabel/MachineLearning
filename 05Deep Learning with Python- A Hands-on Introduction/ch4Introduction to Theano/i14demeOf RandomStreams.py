from theano.tensor.shared_randomstreams import RandomStreams
from theano import function
import numpy

# http://deeplearning.net/software/theano/tutorial/examples.html




for i in range(10):
    # srng = RandomStreams(seed=i)
    srng = RandomStreams(seed=432)
    rv_u = srng.uniform((2,2))
    rv_n = srng.normal((2,2))
    f = function([], rv_u, no_default_updates=True) 
    # g = function([], rv_n, no_default_updates=True)    #Not updating rv_n.rng
    g = function([], rv_n, no_default_updates=True)    #Not updating rv_n.rng

    nearly_zeros = function([], rv_u + rv_u - 2 * rv_u)
    print('f=', f(), 'g=',g(), 'nearly_zeros=',nearly_zeros())