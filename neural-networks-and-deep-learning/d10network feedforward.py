import numpy as np


sizes = [2, 3, 1]
biases = [np.random.randn(y, 1) for y in sizes[1:]]
weights = [np.random.randn(y, x)
            for x, y in zip(sizes[:-1], sizes[1:])]

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def feedforward(a):
    for b, w in zip(biases, weights):
        a = sigmoid(np.dot(w, a)+b)
        return a

def mock_data():
    result = []
    for i in range(10):
        a = np.random.randn(3*3, 1)
        b = np.random.randn(2, 1)
        c = zip(a, b)
        result.append(c)
    print('list(result[9])=',c,list(result[9]))
    return result
    
print('weights>', weights)