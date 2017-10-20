import numpy as np
from termcolor import colored

class Node(object):

    def __init__(self, threshold):
        self.threshold = threshold
        self.output = None

    def input(self, x):
        result = 1 if sum(x) + self.threshold > 0 else 0
        self.output = result

def main():
    t = Node(3)
    x = [-2, -2]
    t.input(x)
    print(t.threshold,'#', t.output)
    x = [-2, 0]
    t.input(x)
    print(t.threshold,'#', t.output)
    

if __name__ == "__main__":
    main()