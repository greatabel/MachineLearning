import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf


sess = tf.InteractiveSession() 
x = tf.constant([[2, 5, 3, -5], 
              [0, 3,-2,  5], 
              [4, 3, 5,  3], 
              [6, 1, 4,  0]]) 
listx = tf.constant([1,2,3,4,5,6,7,8]) 
listy = tf.constant([4,5,8,9]) 
 
print("\nx=\n", x.eval())
print("\nlistx=", listx.eval())
print("\nlisty=", listy.eval())
 
boolx = tf.constant([[True,False], [False,True]]) 
 
print("\ntf.argmin(x, 1).eval() ")# Position of the min value of columns
print(tf.argmin(x, 1).eval() )# Position of the min value of columns

print("\ntf.argmax(x, 1).eval() ")# Position of the max value of rows 
print(tf.argmax(x, 1).eval() )# Position of the max value of rows 

print("\ntf.setdiff1d(listx, listy)[0].eval() ")# List differences 
print(tf.setdiff1d(listx, listy)[0].eval() )# List differences 

print(tf.where(boolx).eval() )# Show true values  

print(tf.unique(listx)[0].eval() )# Unique values in list 
