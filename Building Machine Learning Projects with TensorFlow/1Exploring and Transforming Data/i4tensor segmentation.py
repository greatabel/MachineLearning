import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf


sess = tf.InteractiveSession() 
seg_ids = tf.constant([0,1,1,2,2]) # Group indexes : 0|1,2|3,4 


tens1 = tf.constant([[2, 5, 3, -5], 
                 [0, 3,-2,  5], 
                 [4, 3, 5,  3], 
                 [6, 1, 4,  0], 
                 [6, 1, 4,  0]])  # A sample constant m

print('seg_ids->', seg_ids.eval())
print('tens1->', tens1.eval())

tf.segment_sum(tens1, seg_ids).eval()   # Sum segmen
tf.segment_prod(tens1, seg_ids).eval() # Product segmen
tf.segment_min(tens1, seg_ids).eval() # minimun value goes to
tf.segment_max(tens1, seg_ids).eval() # maximum value goes to
tf.segment_mean(tens1, seg_ids).eval() # mean value goes to group 