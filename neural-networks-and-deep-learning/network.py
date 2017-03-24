import random
import numpy as np


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        print("\n self.num_layers = ", self.num_layers,
              "\n self.sizes = ", self.sizes,
              "\n self.biases = ", self.biases)