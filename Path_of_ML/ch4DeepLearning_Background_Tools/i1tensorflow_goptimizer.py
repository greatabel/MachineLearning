import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets('../../DataSet/MNIST_data', one_hot=True)

x = tf.placeholder("float", [None, 784]) # 输入占位符
W = tf.Variable(tf.zeros([784,10])) # 模型变量
b = tf.Variable(tf.zeros([10])) # 模型变量
y = tf.nn.softmax(tf.matmul(x,W) + b) # 模型

y_pred = tf.placeholder("float", [None,10]) # 输出占位符
cross_entropy = - tf.reduce_sum(y_pred * tf.log(y)) # 交叉熵损失函数
# 优化器，以0.01的学习速率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy) 

sess = tf.Session()
sess.run(tf.global_variables_initializer())


for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(128)
    sess.run(train_step, feed_dict={x: batch_xs, y_pred: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
t = sess.run(accuracy, feed_dict={x: mnist.test.images, y_pred: mnist.test.labels})
print('t=', t)