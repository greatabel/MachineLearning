import sklearn.datasets
import numpy
import pylab
import theano.tensor as T
import theano
import downhill

#Specifiy the number of examples we need (5000) and the noise level
train_X, train_y = sklearn.datasets.make_moons(5000, noise=0.1)
#One hot encode the target values
train_y_onehot = numpy.eye(2)[train_y]
#Plot the data
pylab.scatter(train_X[:-1000, 0], train_X[:-1000, 1], c=train_y[:-1000], cmap=pylab.
cm.Spectral)
# pylab.show()



#Set Seed
numpy.random.seed(0)
num_examples = len(train_X)
#Our Neural Network
nn_input_dim = 2
nn_hdim = 1000
nn_output_dim = 2
#Regularization
reg_lambda = numpy.float64(0.01)
#Weights and bias terms
W1_val = numpy.random.randn(nn_input_dim, nn_hdim)
b1_val = numpy.zeros(nn_hdim)
W2_val = numpy.random.randn(nn_hdim, nn_output_dim)
b2_val = numpy.zeros(nn_output_dim)
X = T.matrix('X')
y = T.matrix('y')
W1 = theano.shared(W1_val, name='W1')
b1 = theano.shared(b1_val, name='b1')
W2 = theano.shared(W2_val, name='W2')
b2 = theano.shared(b2_val, name='b2')
batch_size = 1
#Our Loss function
z1 = X.dot(W1) + b1
a1 = T.tanh(z1)
z2 = a1.dot(W2) + b2
y_hat = T.nnet.softmax(z2)
loss_reg = 1./batch_size * reg_lambda/2 * (T.sum(T.sqr(W1)) + T.sum(T.sqr(W2)))
loss = T.nnet.categorical_crossentropy(y_hat, y).mean() + loss_reg
prediction = T.argmax(y_hat, axis=1)
predict = theano.function([X], prediction)


#Store the training and vlidation loss
train_loss = []
validation_loss = []
opt = downhill.build('sgd', loss=loss)
#Set up training and validation dataset splits, use only one example in a batch 
#and use only one batch per step/epoc
#Use everything except last 1000 examples for training
train = downhill.Dataset([train_X[:-1000], train_y_onehot[:-1000]], batch_size=batch_size,
iteration_size=1)
#Use last 1000 examples for valudation
valid = downhill.Dataset([train_X[-1000:], train_y_onehot[-1000:]])
#SGD
iterations = 0
for tm, vm in opt.iterate(train, valid, patience=10000):
    iterations += 1
    # Record the training and validation loss
    train_loss.append(tm['loss'])
    validation_loss.append(vm['loss'])
    if iterations > 1000:
        break

def build_model(algo):
    loss_value = []
    W1.set_value(W1_val)
    b1.set_value(b1_val)
    W2.set_value(W2_val)
    b2.set_value(b2_val)
    opt = downhill.build(algo, loss=loss)
    train = downhill.Dataset([train_X[:-1000], train_y_onehot[:-1000]], batch_size=1,
    iteration_size=1)
    valid = downhill.Dataset([train_X[-1000:], train_y_onehot[-1000:]])
    iterations = 0
    for tm, vm in opt.iterate(train, valid, patience=1000):
        iterations += 1
        loss_value.append(vm['loss'])
        if iterations > 1000:
            break
    return loss_value
    
algo_names = ['adadelta', 'adagrad', 'adam', 'nag', 'rmsprop', 'rprop', 'sgd']
losses = []
for algo_name in algo_names:
    print(algo_name)
    vloss = build_model(algo_name)
    losses.append(numpy.array(vloss))