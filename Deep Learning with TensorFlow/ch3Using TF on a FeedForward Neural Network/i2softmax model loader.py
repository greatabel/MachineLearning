import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


# logs_path = 'log_mnist_softmax'
mypath = "../../DataSet/MNIST_data/"
mnist = input_data.read_data_sets(mypath, one_hot=True)

sess = tf.InteractiveSession()
new_saver = tf.train.import_meta_graph(mypath + "/saved_mnist_cnn.ckpt.meta")
new_saver.restore(sess, mypath + "/saved_mnist_cnn.ckpt")

tf.get_default_graph().as_graph_def()

try:
    x = sess.graph.get_tensor_by_name("input:0")
    # x = tf.transpose(x)
    y_conv = sess.graph.get_tensor_by_name("output:0")
    image_b = mnist.test.images[100]

    result = sess.run(y_conv, feed_dict={x:[image_b]})
    print('result-->',result)
    print('sess.run(tf.argmax(result, 1))->', sess.run(tf.argmax(result, 1)))

    plt.imshow(image_b.reshape([28, 28]), cmap='Greys')
    plt.show()
except Exception as ex:
    print('error->', ex)
    raise
