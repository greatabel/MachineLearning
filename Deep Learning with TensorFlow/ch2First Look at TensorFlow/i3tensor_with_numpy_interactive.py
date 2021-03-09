import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np


tensor_3d = np.array([[[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8]],
                      [[ 9, 10, 11],[12, 13, 14],[15, 16, 17]],
                      [[18, 19, 20],[21, 22, 23],[24, 25, 26]]])



# tensor_3d = tf.Variable(tensor_3d)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(tensor_3d.get_shape())
#     print(sess.run(tensor_3d))

tensor_3d = tf.convert_to_tensor(tensor_3d, dtype=tf.float64)

with tf.Session() as sess:
    print(tensor_3d.get_shape())
    print(sess.run(tensor_3d))


interactive_session = tf.InteractiveSession()
tensor = np.array([1, 2, 3, 4, 5])
tensor = tf.constant(tensor)
print(tensor.eval())
interactive_session.close()