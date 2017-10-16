import random
import numpy as np
from termcolor import colored

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
    def abel_print(self):
        print(colored('num_layers = ', 'red'), self.num_layers)
        print("sizes = ", self.sizes)
        print("biases = ", self.biases)
        print(colored('weights = ','red'), self.weights)


if __name__ == "__main__":
    net = Network([3*3, 4, 2])
    net.abel_print()
    # net.SGD(training_data, 3, 2, 3.0, test_data=test_data)