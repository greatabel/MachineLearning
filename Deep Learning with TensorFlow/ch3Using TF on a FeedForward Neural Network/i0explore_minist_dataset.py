import numpy as np
import matplotlib.pyplot as plt
# import mnist_data

import gzip
import os
import tempfile

import numpy
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/mnist/input_data.py
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

# mypath = "/Users/wanchang/Downloads/AbelProject/" + \
# "MachineLearning/Deep Learning with TensorFlow/" + \
# "ch3Using TF on a FeedForward Neural Network/MNIST_data/"
mypath = "./MNIST_data/"
__input = read_data_sets(mypath)
print("__input.train.images.shape=", __input.train.images.shape)
print("__input.train.labels.shape=", __input.train.labels.shape)

