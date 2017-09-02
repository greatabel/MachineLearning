from  i1network  import Network, sigmoid

net = Network([2,3,1])
net.abel_print()
print('sigmoid(10)=', sigmoid(10))

import i2mnist_loader
training_data, validation_data, test_data = i2mnist_loader.load_data_wrapper()
training_data = list(training_data)

'''
# ---------------------
# - network.py example:
import network

'''

import i1network
import time

tic = time.clock()
net = i1network.Network([784, 30, 10])

net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

toc = time.clock()
print("time=",toc - tic)