from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

# mypath = "/Users/wanchang/Downloads/AbelProject/" + \
# "MachineLearning/Deep Learning with TensorFlow/" + \
# "ch3Using TF on a FeedForward Neural Network/MNIST_data/"
mypath = "../../DataSet/MNIST_data/"
__input = read_data_sets(mypath)
print("__input.train.images.shape=", __input.train.images.shape)
print("__input.train.labels.shape=", __input.train.labels.shape)
print("__input.test.images.shape=", __input.test.images.shape)
print("__input.test.labels.shape=", __input.test.labels.shape)