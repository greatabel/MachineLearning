import numpy as np
from termcolor import colored
import matplotlib.pyplot as plt
# https://matplotlib.org/users/pyplot_tutorial.html


class Node(object):

    def __init__(self, id, threshold):
        self.id = id
        self.threshold = threshold

    def input(self, w, x):

        w = w.T
        isum = np.dot(x, w)
        # result = 1 if isum + self.threshold > 0 else 0
        z = isum + self.threshold
        result = sigmoid(z)
        self.output = result

def step_function(z):
    result = 1 if z > 0 else 0
    return result

# sigmoid = S字形的, 反曲式的
def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))

def test_sigmoid():
    x = []
    y = []
    z = []
    for i  in range(-20,20):
        x.append(i)
        y.append(sigmoid(i))
        z.append(step_function(i))
    plt.plot(x, y, 'r--', x, z,'bs')
    plt.show()


def main():
    # print('#'*10, 'begin test_sigmoid')
    # test_sigmoid()
    # print('#'*10, 'end test_sigmoid')

    t = Node('id1', -10)
    x = [0, 1, 1]
    w = [3, 3, 10]
    w = np.array(w)
    x = np.array(x)
    t.input(w, x)
    print(t.threshold,'#', t.output)


if __name__ == "__main__":
    main()