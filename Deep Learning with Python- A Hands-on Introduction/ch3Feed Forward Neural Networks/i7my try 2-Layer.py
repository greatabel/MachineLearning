import autograd.numpy as np
import autograd.numpy.random as npr

from termcolor import colored

examples = 4
features = 3
D = (npr.randn(examples, features), npr.randn(examples))
print(colored('输入数据和输出数据 =>', 'red'), D[0],'\n\nD[1]->', D[1])

layer1_units = 2
layers_units = 1
w1 = npr.rand(features, layer1_units)
b1 = npr.rand(layer1_units)
w2 = npr.rand(layer1_units, layers_units)
b2 = 0.0

theta = (w1, b1, w2, b2)
print(colored('theta =>', 'blue'), theta[0],'\ntheta[1]->',theta[1],
    '\ntheta[2]->',theta[2],'\ntheta[3]->',theta[3])

def squared_loss(y, y_hat):
    return np.dot((y - y_hat), (y - y_hat))

def neural_network(x, theta):
    w1, b1, w2, b2 = theta
    return np.tanh(np.dot((np.tanh(np.dot(x,w1) + b1)), w2) + b2)

# def objective(theta, idx):

if __name__ == "__main__":
    print('D[0][0]=', D[0][0])
    print('D[0][1]=', D[0][1])

