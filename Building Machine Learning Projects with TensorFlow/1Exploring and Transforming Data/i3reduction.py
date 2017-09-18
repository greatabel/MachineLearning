import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

sess = tf.InteractiveSession() 
x = tf.constant([[1,  2, 3], 
                  [3,  2, 1], 
                  [-1,-2,-3]]) 
print('x=', x.eval())
boolean_tensor = tf.constant(
        [[True,  False, True], 
          [False, False, True], 
        [True, False, False]])
print("\ntf.reduce_prod(x, reduction_indices=1).eval()" )# reduce pro
print(tf.reduce_prod(x, reduction_indices=1).eval() )# reduce pro

print("\ntf.reduce_min(x, reduction_indices=1).eval()" )# reduce mi
print(tf.reduce_min(x, reduction_indices=1).eval() )# reduce mi

print("\ntf.reduce_max(x, reduction_indices=1).eval()")# reduce ma
print(tf.reduce_max(x, reduction_indices=1).eval() )# reduce ma

print(tf.reduce_mean(x, reduction_indices=1).eval() )# reduce mea
print(tf.reduce_all(boolean_tensor, reduction_indices=1).eval() )# reduce al
print(tf.reduce_any(boolean_tensor, reduction_indices=1).eval() )# reduce any 
