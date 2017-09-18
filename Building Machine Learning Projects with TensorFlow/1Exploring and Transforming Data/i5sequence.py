import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

In [1]: import tensorflow as tf 
In [2]: sess = tf.InteractiveSession() 
In [3]: x = tf.constant([[2, 5, 3, -5], 
...:                  [0, 3,-2,  5], 
...:                  [4, 3, 5,  3], 
...:                  [6, 1, 4,  0]]) 
In [4]: listx = tf.constant([1,2,3,4,5,6,7,8]) 
In [5]: listy = tf.constant([4,5,8,9]) 
 
In [6]: 
 
In [6]: boolx = tf.constant([[True,False], [False,True]]) 
 
In [7]: tf.argmin(x, 1).eval() # Position of the maximum value of columns 
Out[7]: array([3, 2, 1, 3]) 
 
In [8]: tf.argmax(x, 1).eval() # Position of the minimum value of rows 
Out[8]: array([1, 3, 2, 0])

In [9]: tf.listdiff(listx, listy)[0].eval() # List differences 
Out[9]: array([1, 2, 3, 6, 7], dtype=int32) 
 
In [10]: tf.where(boolx).eval() # Show true values 
Out[10]: 
array([[0, 0], 
[1, 1]]) 
 
In [11]: tf.unique(listx)[0].eval() # Unique values in list 
Out[11]: array([1, 2, 3, 4, 5, 6, 7, 8], dtype=int32)