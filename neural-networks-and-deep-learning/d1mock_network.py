import random
import numpy as np
from termcolor import colored

def demo_shuffle():
    arr = np.arange(10)
    print('arr->', arr)
    np.random.shuffle(arr)
    print('arr->', arr)

def mock_data():
    result = []
    for i in range(10):
        a = np.random.randn(3*3, 1)
        b = np.random.randn(2, 1)
        c = zip(a, b)
        result.append(c)
    print('list(result[9])=',c,list(result[9]))
    return result


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

    def SGD(self, training_data, epochs, mini_batch_size, eta,
                test_data=None):
        training_data = list(training_data)
        n = len(training_data)
        print(colored('n =>','red'),n)
        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)
        # for j in range(epochs):
        #     print('-')


if __name__ == "__main__":
    # demo_shuffle()
    # 0 0 1
    # 0 0 0    -> a,b 之一
    # 0 0 1
    training_data, validation_data, test_data = mock_data(),mock_data(),mock_data()
    net = Network([3*3, 4, 2])
    net.abel_print()
    net.SGD(training_data, 30, 5, 3.0, test_data=test_data)
    # net.SGD(training_data, 3, 2, 3.0, test_data=test_data)