import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf


sess = tf.InteractiveSession() 
x = tf.constant([[2, 5, 3, -5], 
              [0, 3,-2,  5], 
              [4, 3, 5,  3], 
              [6, 1, 4,  0]]) 

y = tf.constant([[4, -7, 4, -3, 4], 
              [6, 4,-7,  4, 7], 
              [2, 3, 2,  1, 4], 
              [1, 5, 5,  5, 2]]) 
floatx = tf.constant([[2., 5., 3., -5.], 
                   [0., 3.,-2.,  5.], 
                   [4., 3., 5.,  3.], 
                   [6., 1., 4.,  0.]])

print("tf.transpose(x).eval()->", tf.transpose(x).eval() ) # Transpose matrix ”

print("tf.matmul(x, y).eval()->", tf.matmul(x, y).eval()) # Matrix multiplication 

# Matrix determinant 
print("tf.matrix_determinant(floatx).eval()->", tf.matrix_determinant(floatx).eval() )
# Matrix inverse 
print("tf.matrix_inverse(floatx).eval() ->", tf.matrix_inverse(floatx).eval() )


# Solve Matrix system ”
print("tf.matrix_solve(floatx, [[1],[1],[1],[1]]).eval() ->", tf.matrix_solve(floatx, [[1],[1],[1],[1]]).eval() )
