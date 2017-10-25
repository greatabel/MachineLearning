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
        result = step_function(z)
        self.output = result

def step_function(z):
    result = 1 if z > 0 else 0
    return result
    
def main():
    # 设置阀值接近于0, 权重随便设置成很大的值
    threshold = 0.01
    weight = -10
    nodelist = [Node(i, threshold) for i in range(10)]
    for i in range(10):
        inputs = [1 if i==j else 0  for j in range(10)]
        print(inputs)

if __name__ == "__main__":
    main()