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

def step_function(z):
    result = 1 if z > 0 else 0
    return result
    
def main():
    ""

if __name__ == "__main__":
    main()