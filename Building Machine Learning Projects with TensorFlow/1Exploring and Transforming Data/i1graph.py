import tensorflow as tf 
g = tf.Graph() 
with g.as_default(): 
    sess = tf.Session()
    W_m = tf.Variable(tf.zeros([10, 5])) 
    x_v = tf.placeholder(tf.float32, [None, 10]) 
    result = tf.matmul(x_v, W_m) 
    print(g.as_graph_def())