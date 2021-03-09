import numpy as np
from termcolor import colored

my_hardcode_weights = {
    # 0: [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    # 1: [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    # 2: [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    # 3: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    0: [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    1: [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    2: [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    3: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

class Node(object):

    def __init__(self, id, threshold):
        self.id = id
        self.threshold = threshold

    def set_weights(self, w):
        self.weights = w

    def input(self, w, x):
        # print('input w, x=>', w, x)
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
    print(np.array([10,20]), np.array([10,20]) * 10)
    # 设置阀值接近于0, 权重随便设置成很大的值
    threshold = 0.01
    weight = -10
    layer1_length = 10
    layer2_length = 4
    nodelist_layer1 = [Node(i, threshold) for i in range(layer1_length)]
    nodelist_layer2 = [Node(i, threshold) for i in range(layer2_length)]
    for key, value in my_hardcode_weights.items():
        nodelist_layer2[key].set_weights(value)

    for i in range(layer1_length):
        inputs = [1 if i==j else 0  for j in range(layer1_length)]
        # inputs = [0 if i==j else 1  for j in range(layer1_length)]
        # print('i=', i, 'inputs=>', inputs)
        # 对于输入层的上一层 输入值0/1， 只有单连接权重是-10
        outputs = []
        for node in nodelist_layer2:
            node.input(np.array([node.weights]) * weight, np.array([inputs]))
            output = node.output
            outputs.append(output)
            # print('no#', node.id,'output>', output, node.weights)
        print('1s layer output, 2d layer input >', outputs)
        

        

if __name__ == "__main__":
    main()