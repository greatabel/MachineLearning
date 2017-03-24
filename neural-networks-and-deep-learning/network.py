import random
import numpy as np
import pprint


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                            for x,y in zip(sizes[:-1], sizes[1:])]
        print("sizes[1:], sizes[:-1] = ",sizes[1:], sizes[:-1])
        print("\n self.num_layers = ", self.num_layers,
              "\n self.sizes = ", self.sizes,
              "\n typeof(biases)=", type(self.biases),
              "\n typeof(weights)=", type(self.weights),
             )

        pp = pprint.PrettyPrinter(indent=4)
        print('\nbiases=') 
        pp.pprint(self.biases)
        print('\nweights=') 
        pp.pprint(self.weights)  