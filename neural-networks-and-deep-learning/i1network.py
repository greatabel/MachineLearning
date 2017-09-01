import random
import numpy as np


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) 
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def abel_print(self):
        print("num_layers = ", self.num_layers)
        print("sizes = ", self.sizes)
        print("biases = ", self.biases)
        print("weights = ", self.weights)
        
    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta,
        test_data=None):
        training_data = list(training_data)
        n = len(training_data)

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))