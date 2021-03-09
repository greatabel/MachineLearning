import numpy as np
import matplotlib.pyplot as plt
# import mnist_data
# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python
import gzip
import os
import tempfile

import numpy
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/mnist/input_data.py
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

# mypath = "/Users/wanchang/Downloads/AbelProject/" + \
# "MachineLearning/Deep Learning with TensorFlow/" + \
# "ch3Using TF on a FeedForward Neural Network/MNIST_data/"
mypath = "../../DataSet/MNIST_data/"
__input = read_data_sets(mypath)
print("__input.train.images.shape=", __input.train.images.shape)
print("__input.train.labels.shape=", __input.train.labels.shape)
print("__input.test.images.shape=", __input.test.images.shape)
print("__input.test.labels.shape=", __input.test.labels.shape)

image_0 = __input.train.images[0]
image_0 = np.resize(image_0, (28,28))

label_0 = __input.train.labels[0]
print('label_0 ->', label_0)

plt.imshow(image_0, cmap='Greys_r')
plt.show()