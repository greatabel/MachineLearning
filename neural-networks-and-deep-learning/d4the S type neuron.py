import numpy as np
from termcolor import colored

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

# sigmoid = S字形的, 反曲式的
def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))

def main():
    t = Node('id1', -10)
    x = [0, 1, 1]
    w = [3, 3, 10]
    w = np.array(w)
    x = np.array(x)
    t.input(w, x)
    print(t.threshold,'#', t.output)


if __name__ == "__main__":
    main()