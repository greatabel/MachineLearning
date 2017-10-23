import numpy as np
from termcolor import colored

class Node(object):

    def __init__(self, id, threshold):
        self.id = id
        self.threshold = threshold

    def input(self, x):
        result = 1 if sum(x) + self.threshold > 0 else 0
        self.output = result

def main():
    # t = Node(3)
    # x = [-2, -2]
    # t.input(x)
    # print(t.threshold,'#', t.output)
    # x = [-2, 0]
    # t.input(x)
    # print(t.threshold,'#', t.output)
    threshold = 3
    weight = -2
    nodelist = [Node(i, threshold) for i in range(5)]
    for x1 in (0, 1):
        for x2 in (0, 1):
            # if x1 == 1 and x2 == 1:
            nodelist[0].input([x1 * weight, x2 * weight])
            n0 = nodelist[0].output
            # print('x1, x2 =>',x1, x2, 'n0=>', n0)
            nodelist[1].input([x1 * weight, n0 * weight])
            n1 = nodelist[1].output
            # print('n1 * weight, x2 * weight=>', n1 * weight, x2 * weight)
            nodelist[2].input([n0 * weight, x2 * weight])
            n2 = nodelist[2].output
            nodelist[3].input([n0 * weight, n0 * weight])
            n3 = nodelist[3].output
            # print('n1, n2', n1, n2)
            nodelist[4].input([n1 * weight, n2 * weight])
            n4 = nodelist[4].output
            print('x1, x2 =>', x1, x2,'#', n4, '#', n3)
    

if __name__ == "__main__":
    main()