import numpy as np
from termcolor import colored

#----start of code not relevant to d10 -------#
def show(text):
    return colored(text,'magenta',attrs=['reverse', 'blink'])

sizes = [2,4,3]
biases = [np.random.randn(y, 1) for y in sizes[1:]]
weights = [np.random.randn(y, x)
            for x, y in zip(sizes[:-1], sizes[1:])]

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def feedforward(a):
    print('type(a)=', type(a), a)
    for b, w in zip(biases, weights):
        # print('b, w>', b, w, b.shape, w.shape)
        a = sigmoid(np.dot(w, a)+b)
    # print(show('a='), a)
    return a



#----end of code not relevant to d10 -------#
def mock_data(mock_count):
    datas = []
    for i in range(mock_count):
        a = np.random.randn(2, 1)
        b = np.random.randn(3, 1)
        datas.append((a,b))
    # print('list(result[9])=',c,list(result[9]))
    return datas

test_data = mock_data(100)
hits = 0
for item in test_data:

    t1 = item[0]
    t2 = item[1]
    # print(np.argmax(feedforward(t1)))
    test_results = [(np.argmax(feedforward(t1)), np.argmax(t2))]
    print('test_results=', test_results)
    hit = sum(int(x == y) for (x, y) in test_results)          
    hits += hit
print(show('hits='), hits)