import numpy as np
from termcolor import colored


def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

sizes = [2, 3, 2]
layers = len(sizes)
biases = [np.random.randn(y, 1)
            for y in sizes[1:]]
weights = [np.random.randn(y, x)
            for x, y in zip(sizes[:-1], sizes[1:])] 
                       
print('biases=', biases)
print('weights=', weights)
