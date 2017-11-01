import numpy as np
from termcolor import colored

def show(text):
    return colored(text,'magenta',attrs=['reverse', 'blink'])
sizes = [2, 3, 1]
biases = [np.random.randn(y, 1) for y in sizes[1:]]
weights = [np.random.randn(y, x)
            for x, y in zip(sizes[:-1], sizes[1:])]

# def test_np_argmax():
#     a = np.arange(6).reshape(2,3)
#     print(a, colored('np.argmax=','blue'),np.argmax(a))
# test_np_argmax()

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))


def feedforward(a):
    for b, w in zip(biases, weights):
        print('b.shape, w.shape >', b.shape, w.shape)
        print(colored('w=','red'), w,'a=', a, 'b>', b, )
        t0 = np.dot(w, a)
        print('np.dot(w, a) =', t0, t0.shape)
        t = t0+b
        print('(t0+b)=', t, t.shape)
        a = sigmoid(t)
        print(show('out a>'), a)
    return a

print('biases>', biases)   
print('weights>', weights)

a = np.array([[10],[20]])
print('a = ', a, a.shape)
result = feedforward(a)
print(colored('result>','blue'), result)
