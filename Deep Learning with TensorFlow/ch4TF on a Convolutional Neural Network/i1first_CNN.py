import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../MNIST_data", one_hot=True)


batch_size = 128
test_size = 256

img_size = 28
num_classes = 10

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))


X = tf.placeholder("float", [None, img_size, img_size, 1])
Y = tf.placeholder("float", [None, num_classes])

trX, trY, teX, teY = mnist.train.images,\
                     mnist.train.labels, \
                     mnist.test.images, \
                     mnist.test.labels

trX = trX.reshape(-1, img_size, img_size, 1)  # 28x28x1 input img
teX = teX.reshape(-1, img_size, img_size, 1)  # 28x28x1 input img

w = init_weights([3, 3, 1, 32])       # 3x3x1 conv, 32 outputs
w2 = init_weights([3, 3, 32, 64])     # 3x3x32 conv, 64 outputs
w3 = init_weights([3, 3, 64, 128])    # 3x3x32 conv, 128 outputs
w4 = init_weights([128 * 4 * 4, 625]) # FC 128 * 4 * 4 inputs, 625 outputs
w_o = init_weights([625, num_classes])         # FC 625 inputs, 10 outputs (labels)
