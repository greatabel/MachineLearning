import sklearn.datasets
import numpy
import pylab


#Specifiy the number of examples we need (5000) and the noise level
train_X, train_y = sklearn.datasets.make_moons(5000, noise=0.1)
#One hot encode the target values
train_y_onehot = numpy.eye(2)[train_y]
#Plot the data
pylab.scatter(train_X[:-1000, 0], train_X[:-1000, 1], c=train_y[:-1000], cmap=pylab.
cm.Spectral)
pylab.show()