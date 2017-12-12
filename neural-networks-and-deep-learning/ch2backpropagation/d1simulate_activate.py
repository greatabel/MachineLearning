import numpy as np
from termcolor import colored


def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

sizes = [2, 3, 2]
print('sizes[:-1]=', sizes[:-1])
print('sizes[1:]=', sizes[1:])
for item in zip(sizes[:-1], sizes[1:]):
    print('item=', item)
    
layers = len(sizes)
biases = [np.random.randn(y, 1)
            for y in sizes[1:]]
weights = [np.random.randn(y, x)
            for x, y in zip(sizes[:-1], sizes[1:])]




print('weights=', weights)

activates = [np.array([1,2]), np.array([3,4]), np.array([5,6])]

s0 = weights[0] * activates 
s1 = np.transpose(s0)
s2 = s1[0] + s1[1]
b0 = np.concatenate((biases[0][0], biases[0][1],biases[0][2]))
s3 = s2 + b0

print('a1=', sigmoid(s3))