import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

# for i in range(1,10):
#     print("i= ", i)
#     print(sigmoid(i))

# derivative of sigmoid
# sigmoid(y) * (1.0 - sigmoid(y))
# the way we use this y is already sigmoided
def dsigmoid(y):
    return y * (1.0 - y)    

class MLP_NeuralNetwork(object):

    def __init__(self, input, hidden, output):
        """
        :param input: number of input neurons
        :param hidden: number of hidden neurons
        :param output: number of output neurons
        """
        self.input = input + 1 # add 1 for bias node
        self.hidden = hidden
        self.output = output

        # set up array of 1s for actviations
        self.ai = [1.0] * self.input
        self.ah = [1.0] * self.hidden
        self.ao = [1.0] * self.output

        # create randomized weight
        self.wi = np.random.randn(self.input, self.hidden)
        self.wo = np.random.randn(self.hidden, self.output)

        # create arrays of 0 for changes
        self.ci = np.zeros((self.input, self.hidden))
        self.co = np.zeros((self.hidden, self.output))


