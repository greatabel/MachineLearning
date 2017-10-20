import numpy as np
from termcolor import colored

class Node(object):

    def __init__(self, threshold):
        self.threshold = threshold

    def output(self, x):
        return 1 if sum(x) + self.threshold > 0 else 0

def main():
    t = Node(3)
    x = [-2, -2]
    output = t.output(x)
    print(t.threshold,'#', output)
    x = [-2, 0]
    output = t.output(x)
    print(t.threshold,'#', output)
    

if __name__ == "__main__":
    main()