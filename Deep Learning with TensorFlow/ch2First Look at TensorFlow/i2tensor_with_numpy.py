import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np

tensor_1d = np.array([1,2,3,4,5,6,7,8,9,10])
tensor_1d = tf.constant(tensor_1d)
with tf.Session() as sess:
    print(tensor_1d.get_shape())
    print(sess.run(tensor_1d))

print('*-' * 20)
# tensor 2d variable
tensor_2d = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
tensor_2d = tf.Variable(tensor_2d)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(tensor_2d.get_shape())
    print(sess.run(tensor_2d))
